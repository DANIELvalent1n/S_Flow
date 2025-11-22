# pages/7_📈_Dashboard.py

import streamlit as st
from modules.database import Database
from modules.utils import format_currency
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard - S_FLOW", layout="wide")

st.title("📈 Dashboard Administrativ")

db = Database()

# Obține statistici
stats = db.get_stats()
df_clients = db.get_all_clients()
df_projects = db.get_all_projects()
df_contacts = db.get_all_contact_requests()
df_reviews = db.get_all_testimonials()

# KPIs principale
st.subheader("📊 Indicatori Cheie de Performanță")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👥 Total Clienți", stats.get("total_clients", 0), 
             delta=None if stats.get("active_clients", 0) == 0 else f"{stats.get('active_clients', 0)} activi")

with col2:
    st.metric("✅ Clienți Activi", stats.get("active_clients", 0))

with col3:
    st.metric("📊 Proiecte", stats.get("total_projects", 0),
             delta=f"{stats.get('completed_projects', 0)} finalizate")

with col4:
    st.metric("💰 Buget Lunar", f"{format_currency(stats.get('total_budget', 0))}")

with col5:
    st.metric("⭐ Rating Mediu", f"{stats.get('avg_rating', 0)}/5")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Grafice", "👥 Clienți", "📋 Proiecte", "💬 Contacte"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Clienți pe Serviciu")
        if not df_clients.empty:
            service_counts = df_clients['service_type'].value_counts()
            fig = px.pie(values=service_counts.values, names=service_counts.index,
                        title="Distribuție Servicii")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Niciun client")
    
    with col2:
        st.subheader("Clienți pe Status")
        if not df_clients.empty:
            status_counts = df_clients['status'].value_counts()
            fig = px.bar(status_counts, title="Distribuție Status Clienți")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Niciun client")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Proiecte pe Status")
        if not df_projects.empty:
            status_counts = df_projects['status'].value_counts()
            fig = px.pie(values=status_counts.values, names=status_counts.index,
                        title="Distribuție Status Proiecte")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Niciun proiect")
    
    with col2:
        st.subheader("Buget Clienți - Top 10")
        if not df_clients.empty:
            top_clients = df_clients.nlargest(10, 'monthly_budget')[['company_name', 'monthly_budget']]
            fig = px.bar(top_clients, x='company_name', y='monthly_budget',
                        title="Top 10 Clienți după Buget")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Niciun client")

with tab2:
    st.subheader("👥 Analiza Clienți")
    
    if not df_clients.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Top 5 Clienți după Buget:**")
            top_5 = df_clients.nlargest(5, 'monthly_budget')[['company_name', 'monthly_budget']]
            for idx, client in top_5.iterrows():
                st.write(f"• {client['company_name']}: {format_currency(client['monthly_budget'])}")
        
        with col2:
            st.write("**Distribuție Servicii:**")
            service_dist = df_clients['service_type'].value_counts()
            for service, count in service_dist.items():
                st.write(f"• {service}: {count}")
        
        with col3:
            st.write("**Distribuție Status:**")
            status_dist = df_clients['status'].value_counts()
            for status, count in status_dist.items():
                st.write(f"• {status}: {count}")
        
        st.markdown("---")
        
        st.write("**Tabel Complet Clienți:**")
        st.dataframe(
            df_clients[['company_name', 'contact_name', 'email', 'service_type', 'monthly_budget', 'status']],
            use_container_width=True
        )
    else:
        st.info("Nu sunt clienți înregistrați.")

with tab3:
    st.subheader("📋 Analiza Proiecte")
    
    if not df_projects.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Proiecte pe Serviciu:**")
            service_dist = df_projects['service'].value_counts()
            for service, count in service_dist.items():
                st.write(f"• {service}: {count}")
        
        with col2:
            st.write("**Proiecte pe Status:**")
            status_dist = df_projects['status'].value_counts()
            for status, count in status_dist.items():
                st.write(f"• {status}: {count}")
        
        with col3:
            st.write("**Statistici Buget:**")
            st.write(f"• Total: {format_currency(df_projects['budget'].sum())}")
            st.write(f"• Mediu: {format_currency(df_projects['budget'].mean())}")
            st.write(f"• Max: {format_currency(df_projects['budget'].max())}")
        
        st.markdown("---")
        
        st.write("**Tabel Complet Proiecte:**")
        st.dataframe(
            df_projects[['project_name', 'company_name', 'service', 'status', 'budget']],
            use_container_width=True
        )
    else:
        st.info("Nu sunt proiecte înregistrate.")

with tab4:
    st.subheader("💬 Analiza Contacte")
    
    if not df_contacts.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Total Contacte Primite:** {len(df_contacts)}")
            
            status_dist = df_contacts['status'].value_counts()
            for status, count in status_dist.items():
                st.write(f"• {status}: {count}")
        
        with col2:
            # Contacte ultimeazile
            from modules.utils import get_date_range_stats
            last_7_days = get_date_range_stats(df_contacts, 'created_at', days=7)
            last_30_days = get_date_range_stats(df_contacts, 'created_at', days=30)
            
            st.write(f"**Contacte Recente:**")
            st.write(f"• Ultimele 7 zile: {last_7_days}")
            st.write(f"• Ultimele 30 zile: {last_30_days}")
        
        st.markdown("---")
        
        st.write("**Contacte Recente:**")
        recent = df_contacts.sort_values('created_at', ascending=False).head(10)
        st.dataframe(
            recent[['name', 'email', 'subject', 'status']],
            use_container_width=True
        )
    else:
        st.info("Nu sunt contacte înregistrate.")

st.markdown("---")

# Footer
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Recenzii", len(df_reviews))

with col2:
    if not df_reviews.empty:
        avg_rating = df_reviews['rating'].mean()
        st.metric("Rating Mediu", f"{avg_rating:.1f}/5")
    else:
        st.metric("Rating Mediu", "N/A")

with col3:
    st.metric("Mesaje Contact", len(df_contacts))

st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px; margin-top: 40px;">
    <p>© 2025 S_FLOW - Dashboard Administrativ</p>
    <p>Ultima actualizare: in timp real</p>
</div>
""", unsafe_allow_html=True)