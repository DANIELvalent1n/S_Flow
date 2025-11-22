# pages/4_📊_Proiecte.py

import streamlit as st
from modules.database import Database
from modules.utils import format_currency, get_progress_bar, display_success_message, display_error_message
import pandas as pd

st.set_page_config(page_title="Proiecte - S_FLOW", layout="wide")

st.title("📊 Gestionare Proiecte")

db = Database()

# Tabs
tab1, tab2, tab3 = st.tabs(["➕ Nou Proiect", "📋 Lista Proiecte", "📈 Statistici"])

with tab1:
    st.subheader("Adaugă un Proiect Nou")
    
    # Obține lista clienți
    df_clients = db.get_all_clients()
    
    if df_clients.empty:
        st.warning("⚠️ Trebuie să adaugi un client înainte de a crea un proiect!")
        if st.button("➕ Adaugă Client"):
            st.switch_page("pages/3_👥_Clienti.py")
    else:
        with st.form("add_project_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                client_name = st.selectbox(
                    "👥 Client *",
                    df_clients['company_name'].tolist()
                )
                client_id = df_clients[df_clients['company_name'] == client_name]['id'].values[0]
                
                project_name = st.text_input("📝 Nume Proiect *")
                description = st.text_area("📄 Descriere", height=80)
            
            with col2:
                service = st.selectbox("🛠️ Serviciu *", [
                    "Consultanță IT", "Dezvoltare Software", "Analiză Date", "Training"
                ])
                status = st.selectbox("📊 Status", [
                    "Planificare", "În Curs", "Finalizat", "Suspendat"
                ])
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                start_date = st.date_input("📅 Data Start")
            
            with col2:
                end_date = st.date_input("📅 Data Finalizare")
            
            with col3:
                budget = st.number_input("💰 Buget (lei)", min_value=0, step=100, value=2000)
            
            submitted = st.form_submit_button("✅ Salvează Proiect", use_container_width=True)
            
            if submitted:
                if not project_name or project_name.strip() == "":
                    display_error_message("Completează numele proiectului!")
                elif start_date > end_date:
                    display_error_message("Data de start trebuie să fie înainte de data de finalizare!")
                else:
                    if db.add_project(client_id, project_name, description, service, status, start_date, end_date, budget):
                        display_success_message(f"Proiectul '{project_name}' a fost salvat!")
                        st.rerun()
                    else:
                        display_error_message("Eroare la salvarea proiectului.")

with tab2:
    st.subheader("📋 Lista Proiecte")
    
    df_projects = db.get_all_projects()
    
    if not df_projects.empty:
        # Filtre
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_status = st.multiselect(
                "Filtrează după Status",
                df_projects['status'].unique().tolist(),
                default=df_projects['status'].unique().tolist()
            )
        
        with col2:
            filter_service = st.multiselect(
                "Filtrează după Serviciu",
                df_projects['service'].unique().tolist(),
                default=df_projects['service'].unique().tolist()
            )
        
        with col3:
            sort_by = st.selectbox("Sortează după", ["Data Start", "Stare", "Buget"])
        
        # Aplicare filtre
        df_filtered = df_projects[
            (df_projects['status'].isin(filter_status)) & 
            (df_projects['service'].isin(filter_service))
        ]
        
        # Sortare
        if sort_by == "Data Start":
            df_filtered = df_filtered.sort_values('start_date', ascending=False)
        elif sort_by == "Stare":
            df_filtered = df_filtered.sort_values('status')
        else:
            df_filtered = df_filtered.sort_values('budget', ascending=False)
        
        st.markdown(f"**Total: {len(df_filtered)} proiecte**")
        
        # Afișare proiecte
        for idx, project in df_filtered.iterrows():
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.write(f"**{project['project_name']}**")
                st.caption(f"Client: {project['company_name']}")
            
            with col2:
                st.write(f"🛠️ {project['service']}")
                st.write(f"📅 {str(project['start_date'])} - {str(project['end_date'])}")
                
                # Calculare progres
                from modules.utils import calculate_project_progress
                progress = calculate_project_progress(project['start_date'], project['end_date'], project['status'])
                st.write(get_progress_bar(progress))
            
            with col3:
                if project['status'] == 'Finalizat':
                    st.success(f"✅ {project['status']}")
                elif project['status'] == 'În Curs':
                    st.info(f"🔵 {project['status']}")
                elif project['status'] == 'Planificare':
                    st.warning(f"📋 {project['status']}")
                else:
                    st.error(f"⏸️ {project['status']}")
                
                st.caption(f"💰 {format_currency(project['budget'])}")
            
            st.divider()
        
        # Tabel complet
        st.markdown("---")
        st.subheader("📊 Vizualizare Tabel")
        
        display_cols = ['project_name', 'company_name', 'service', 'status', 'start_date', 'budget']
        st.dataframe(
            df_filtered[display_cols].rename(columns={
                'project_name': 'Proiect',
                'company_name': 'Client',
                'service': 'Serviciu',
                'status': 'Status',
                'start_date': 'Data Start',
                'budget': 'Buget (lei)'
            }),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("📭 Nu există proiecte înregistrate inca.")

with tab3:
    st.subheader("📈 Statistici Proiecte")
    
    df_projects = db.get_all_projects()
    
    if not df_projects.empty:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Proiecte", len(df_projects))
        
        with col2:
            in_progress = len(df_projects[df_projects['status'] == 'În Curs'])
            st.metric("În Curs", in_progress)
        
        with col3:
            completed = len(df_projects[df_projects['status'] == 'Finalizat'])
            st.metric("Finalizate", completed)
        
        with col4:
            total_budget = df_projects['budget'].sum()
            st.metric("Buget Total", f"{total_budget:,.0f} lei")
        
        st.markdown("---")
        
        # Grafice
        try:
            import plotly.express as px
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Distribuție Servicii")
                service_counts = df_projects['service'].value_counts()
                fig = px.bar(
                    x=service_counts.index,
                    y=service_counts.values,
                    labels={'x': 'Serviciu', 'y': 'Număr Proiecte'},
                    title="Proiecte pe Serviciu"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Distribuție Status")
                status_counts = df_projects['status'].value_counts()
                fig = px.pie(
                    values=status_counts.values,
                    names=status_counts.index,
                    title="Proiecte pe Status"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        except Exception as e:
            st.error(f"Eroare la generarea graficelor: {e}")
    else:
        st.info("Nu sunt proiecte pentru a afișa statistici.")