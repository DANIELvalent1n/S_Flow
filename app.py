# app.py - Main Entry Point pentru S_FLOW

import streamlit as st
from config import COMPANY_INFO, THEME_CONFIG

# Configurare pagină
st.set_page_config(
    page_title=f"{COMPANY_INFO['name']} - Consultanță IT",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizat
st.markdown("""
    <style>
        :root {
            --primary: #1f77b4;
            --secondary: #667eea;
            --success: #28a745;
            --danger: #dc3545;
        }
        
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        
        .service-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            border-radius: 4px;
            margin: 10px 0;
        }
        
        h1 {
            color: #1f77b4;
            text-align: center;
            margin-bottom: 10px;
        }
        
        h2 {
            color: #1f77b4;
            border-bottom: 2px solid #1f77b4;
            padding-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("---")
    st.title("🎯 S_FLOW")
    st.markdown(f"*{COMPANY_INFO['tagline']}*")
    st.markdown("---")
    
    st.subheader("📞 Contact Rapid")
    st.write(f"📧 {COMPANY_INFO['email']}")
    st.write(f"📍 {COMPANY_INFO['location']}")
    st.write(f"🕐 {COMPANY_INFO['working_hours']}")
    
    st.markdown("---")
    st.caption("© 2025 S_FLOW - Toate drepturile rezervate")

# Conținut principal
st.title(f"🚀 {COMPANY_INFO['name']}")
st.markdown(f"### {COMPANY_INFO['tagline']}")

st.markdown("---")

# Coloane principale
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Clienți Activi", "15+", "+3 luna aceasta")

with col2:
    st.metric("📊 Proiecte", "42+", "+5 luna aceasta")

with col3:
    st.metric("⭐ Rating", "4.8/5", "18 recenzii")

st.markdown("---")

# Secțiune Despre
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Despre Noi")
    st.write(COMPANY_INFO['description'])
    
    st.subheader("💡 Misiune")
    st.write(COMPANY_INFO['mission'])

with col2:
    st.subheader("👀 Viziune")
    st.write(COMPANY_INFO['vision'])
    
    st.subheader("👥 Fondatori")
    st.write(f"""
    - {COMPANY_INFO['founder_1']}
    - {COMPANY_INFO['founder_2']}
    - {COMPANY_INFO['founder_3']}
    """)

st.markdown("---")

# Servicii principale
st.subheader("📋 Serviciile Noastre")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 💼 Consultanță IT
    **500 - 1500 lei/lună**
    - Audit proceselor
    - Recomandări strategice
    - Plan implementare
    """)

with col2:
    st.markdown("""
    ### 🛠️ Dezvoltare Software
    **1000 - 3000 lei/lună**
    - Aplicații web/desktop
    - Soluții cloud
    - Interfață intuitivă
    """)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Analiză Date
    **800 - 2000 lei/lună**
    - Dashboard-uri vizuale
    - Rapoarte automate
    - Export date
    """)

with col2:
    st.markdown("""
    ### 🎓 Training & Suport
    **600 - 1200 lei/lună**
    - Training angajați
    - Suport 24/7
    - Documentație
    """)

st.markdown("---")

st.subheader("🔗 Navigare Rapidă")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📋 Vezi Servicii", use_container_width=True):
        st.switch_page("pages/2_📋_Servicii.py")

with col2:
    if st.button("📝 Contactează-ne", use_container_width=True):
        st.switch_page("pages/5_💼_Contact.py")

with col3:
    if st.button("⭐ Recenzii", use_container_width=True):
        st.switch_page("pages/6_⭐_Recenzii.py")

st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p><strong>S_FLOW - Transformăm ideile în soluții digitale</strong></p>
    <p>Timișoara, România | Consultanță IT & Digitalizare pentru IMM-uri</p>
</div>
""", unsafe_allow_html=True)