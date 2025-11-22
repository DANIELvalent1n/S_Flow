# pages/3_👥_Clienti.py

import streamlit as st
from modules.database import Database
from modules.utils import get_status_color, display_success_message, display_error_message
import pandas as pd

st.set_page_config(page_title="Clienți - S_FLOW", layout="wide")

st.title("👥 Gestionare Clienți")

db = Database()

# Tabs principale
tab1, tab2, tab3 = st.tabs(["➕ Adaugă Client", "📋 Lista Clienți", "📊 Statistici"])

with tab1:
    st.subheader("Adaugă un Client Nou")
    
    with st.form("add_client_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            company_name = st.text_input("📍 Nume Firmă *")
            contact_name = st.text_input("👤 Persoană de Contact")
            email = st.text_input("📧 Email")
        
        with col2:
            phone = st.text_input("📞 Telefon")
            service_type = st.selectbox("🛠️ Tip Serviciu *", [
                "Consultanță IT", "Dezvoltare Software", "Analiză Date", "Training", "Altul"
            ])
            monthly_budget = st.number_input("💰 Buget Lunar (lei)", min_value=0, step=100, value=1000)
        
        col1, col2 = st.columns(2)
        
        with col1:
            status = st.selectbox("📊 Status", ["Prospect", "Client Activ", "Client Inactiv"])
        
        with col2:
            notes = st.text_area("📝 Note Interne", height=68)
        
        submitted = st.form_submit_button("✅ Salvează Client", use_container_width=True)
        
        if submitted:
            if not company_name:
                display_error_message("Completează numele firmei!")
            else:
                if db.add_client(company_name, contact_name, email, phone, service_type, monthly_budget, status, notes):
                    display_success_message(f"Client '{company_name}' a fost adăugat cu succes!")
                    st.rerun()
                else:
                    display_error_message("Eroare la salvarea clientului.")

with tab2:
    st.subheader("📋 Lista Clienți")
    
    df_clients = db.get_all_clients()
    
    if not df_clients.empty:
        # Filtre
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_status = st.multiselect(
                "Filtrează după Status",
                df_clients['status'].unique().tolist(),
                default=df_clients['status'].unique().tolist()
            )
        
        with col2:
            filter_service = st.multiselect(
                "Filtrează după Serviciu",
                df_clients['service_type'].unique().tolist(),
                default=df_clients['service_type'].unique().tolist()
            )
        
        with col3:
            sort_by = st.selectbox("Sortează după", ["Dată Adăugării", "Nume Firmă", "Buget"])
        
        # Aplicare filtre
        df_filtered = df_clients[
            (df_clients['status'].isin(filter_status)) & 
            (df_clients['service_type'].isin(filter_service))
        ]
        
        # Sortare
        if sort_by == "Dată Adăugării":
            df_filtered = df_filtered.sort_values('created_at', ascending=False)
        elif sort_by == "Nume Firmă":
            df_filtered = df_filtered.sort_values('company_name')
        else:
            df_filtered = df_filtered.sort_values('monthly_budget', ascending=False)
        
        st.markdown(f"**Total: {len(df_filtered)} clienți**")
        
        # Afișare clienți
        for idx, client in df_filtered.iterrows():
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            
            with col1:
                st.write(f"**{client['company_name']}**")
                if client['contact_name']:
                    st.caption(f"Contact: {client['contact_name']}")
            
            with col2:
                if client['email']:
                    st.write(f"📧 {client['email']}")
                if client['phone']:
                    st.caption(f"📞 {client['phone']}")
            
            with col3:
                st.write(f"{get_status_color(client['status'])} {client['status']}")
                st.caption(f"💰 {client['monthly_budget']:.0f} lei/lună")
            
            st.divider()
        
        # Tabel complet
        st.markdown("---")
        st.subheader("📊 Vizualizare Tabel")
        
        display_cols = ['company_name', 'contact_name', 'email', 'service_type', 'monthly_budget', 'status']
        st.dataframe(
            df_filtered[display_cols].rename(columns={
                'company_name': 'Firmă',
                'contact_name': 'Contact',
                'email': 'Email',
                'service_type': 'Serviciu',
                'monthly_budget': 'Buget (lei)',
                'status': 'Status'
            }),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("📭 Nu există clienți înregistrați inca. Adaugă un client nou!")

with tab3:
    st.subheader("📊 Statistici Clienți")
    
    df_clients = db.get_all_clients()
    
    if not df_clients.empty:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Clienți", len(df_clients))
        
        with col2:
            active = len(df_clients[df_clients['status'] == 'Client Activ'])
            st.metric("Activi", active)
        
        with col3:
            prospects = len(df_clients[df_clients['status'] == 'Prospect'])
            st.metric("Prospecți", prospects)
        
        with col4:
            total_budget = df_clients['monthly_budget'].sum()
            st.metric("Buget Lunar Total", f"{total_budget:,.0f} lei")
        
        st.markdown("---")
        
        # Grafice
        try:
            import plotly.express as px
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Distribuție Servicii")
                service_counts = df_clients['service_type'].value_counts()
                fig = px.bar(
                    x=service_counts.index,
                    y=service_counts.values,
                    labels={'x': 'Serviciu', 'y': 'Număr Clienți'},
                    title="Clienți pe Tip Serviciu"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Distribuție Status")
                status_counts = df_clients['status'].value_counts()
                fig = px.pie(
                    values=status_counts.values,
                    names=status_counts.index,
                    title="Clienți pe Status"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Top Clienți după Buget")
                top_clients = df_clients.nlargest(5, 'monthly_budget')[['company_name', 'monthly_budget']]
                top_clients_sorted = top_clients.sort_values('monthly_budget', ascending=True)
                fig = px.barh(
                    x='monthly_budget',
                    y='company_name',
                    data_frame=top_clients_sorted,
                    labels={'monthly_budget': 'Buget (lei)', 'company_name': 'Firmă'},
                    title="Top 5 Clienți"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Rezumat Servicii")
                service_summary = df_clients['service_type'].value_counts()
                for service, count in service_summary.items():
                    st.write(f"• **{service}**: {count} clienți")
        
        except Exception as e:
            st.error(f"Eroare la generarea graficelor: {e}")
    else:
        st.info("Nu sunt clienți pentru a afișa statistici.")