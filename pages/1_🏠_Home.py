# pages/1_🏠_Home.py

import streamlit as st
from config import COMPANY_INFO, OBJECTIVES, DEVELOPMENT_PERSPECTIVES, LEGISLATION
from modules.database import Database

st.set_page_config(page_title="Acasă - S_FLOW", layout="wide")

st.title("🏠 Acasă - S_FLOW")
st.markdown("*Transformăm ideile în soluții digitale!*")

st.markdown("---")

# Statistici rapide
db = Database()
stats = db.get_stats()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Clienți Activi", stats.get("active_clients", 0))

with col2:
    st.metric("📊 Proiecte Total", stats.get("total_projects", 0))

with col3:
    st.metric("✅ Finalizate", stats.get("completed_projects", 0))

with col4:
    st.metric("⭐ Rating Mediu", f"{stats.get('avg_rating', 0)}/5")

st.markdown("---")

# Secțiuni principale
tab1, tab2, tab3, tab4 = st.tabs(["📖 Despre", "🎯 Obiective", "📈 Perspectiva", "⚖️ Legislație"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Despre S_FLOW")
        st.write(COMPANY_INFO['description'])
        
        st.subheader("💼 Misiune")
        st.write(COMPANY_INFO['mission'])
        
        st.subheader("👀 Viziune")
        st.write(COMPANY_INFO['vision'])
    
    with col2:
        st.subheader("📍 Locație")
        st.write(f"**{COMPANY_INFO['location']}**")
        
        st.subheader("📧 Contact")
        st.write(f"Email: {COMPANY_INFO['email']}")
        st.write(f"Telefon: {COMPANY_INFO['phone']}")
        
        st.subheader("🕐 Orari")
        st.write(COMPANY_INFO['working_hours'])
        
        st.subheader("🗺️ Zone Acoperite")
        for zone in COMPANY_INFO['covered_zones']:
            st.write(f"• {zone}")

with tab2:
    st.subheader("🎯 Obiective (3-5 ani)")
    
    for i, objective in enumerate(OBJECTIVES, 1):
        st.markdown(f"**{i}. {objective}**")
        st.markdown("---")

with tab3:
    st.subheader("📈 Perspective de Dezvoltare")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"""
        **3 ANI**
        
        {DEVELOPMENT_PERSPECTIVES['3_years']}
        """)
    
    with col2:
        st.warning(f"""
        **5 ANI**
        
        {DEVELOPMENT_PERSPECTIVES['5_years']}
        """)
    
    with col3:
        st.success(f"""
        **10 ANI**
        
        {DEVELOPMENT_PERSPECTIVES['10_years']}
        """)

with tab4:
    st.subheader("⚖️ Cadrul Legal de Operare")
    
    st.write("""
    S_FLOW activează conform legislației în vigoare din România.
    Toate activitățile sunt conforme cu normele și regulamentele aplicabile.
    """)
    
    st.write("**Acte și Reglementări Principale:**")
    
    for leg in LEGISLATION:
        st.write(f"✓ {leg}")

st.markdown("---")

# Piață și segmente
st.subheader("🎯 Piața Țintă")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Segment Țintă:**
    - IMM-uri cu 5-100 angajați
    - Companii din sectoare variate
    - Firme care doresc digitalizare
    
    **Regiuni Principale:**
    - Timiș
    - Arad
    - Bihor
    - Cluj
    """)

with col2:
    st.write("""
    **Caracteristici Piață:**
    - 20.000-30.000 companii potențiale
    - Creștere constantă
    - Cerere pentru digitalizare
    
    **Buget Mediu Client:**
    - 500 - 3000 lei/lună
    - Flexibil după serviciu
    - Opțiuni de plată diverse
    """)

st.markdown("---")

# Founder info
st.subheader("👥 Echipa Fondatoare")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"""
    **{COMPANY_INFO['founder_1']}**
    
    Manager General
    """)

with col2:
    st.info(f"""
    **{COMPANY_INFO['founder_2']}**
    
    Manager Tehnic
    """)

with col3:
    st.info(f"""
    **{COMPANY_INFO['founder_3']}**
    
    Manager Operațional
    """)

st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px; margin-top: 40px;">
    <p>© 2025 S_FLOW - Consultanță IT și Digitalizare</p>
</div>
""", unsafe_allow_html=True)