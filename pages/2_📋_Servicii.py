# pages/2_📋_Servicii.py

import streamlit as st
from config import SERVICES, COMPANY_INFO
from modules.utils import format_currency

st.set_page_config(page_title="Servicii - S_FLOW", layout="wide")

st.title("📋 Serviciile Noastre")
st.markdown("Soluții IT adaptate nevoilor tale de business")

st.markdown("---")

# Introducere
st.markdown("""
S_FLOW oferă o gamă completă de servicii dedicate digitalizării și optimizării proceselor 
firmelor mici și mijlocii. Prețurile sunt competitive, iar serviciile sunt personalizate 
pentru fiecare client.
""")

st.markdown("---")

# Afișare servicii
st.subheader("🎯 Portofoliul Nostru de Servicii")

for service_key, service in SERVICES.items():
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {service['name']}")
            st.write(service['description'])
            
            st.write("**Caracteristici incluse:**")
            for feature in service['features']:
                st.write(f"✓ {feature}")
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 20px; border-radius: 10px; text-align: center;">
                <h4>Preț</h4>
                <p style="font-size: 24px; margin: 10px 0;">
                    {format_currency(service['price_min'])} - {format_currency(service['price_max'])}
                </p>
                <p style="font-size: 12px;">per {service['unit']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")

# Comparație servicii
st.subheader("📊 Comparație Servicii")

comparison_data = {
    "Serviciu": ["Consultanță IT", "Dezvoltare Software", "Analiză Date", "Training"],
    "Preț Mediu": [
        f"{format_currency((500+1500)/2)}",
        f"{format_currency((1000+3000)/2)}",
        f"{format_currency((800+2000)/2)}",
        f"{format_currency((600+1200)/2)}"
    ],
    "Durata Medie": ["Continuu", "3-6 luni", "Continuu", "2-4 săptămâni"],
    "Complexitate": ["Medie", "Înaltă", "Medie", "Scăzută"]
}

st.dataframe(comparison_data, use_container_width=True)

st.markdown("---")

# Pachet personalizat
st.subheader("🎁 Pachete Personalizate")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Pachet STARTER** (500 - 800 lei/lună)
    - Consultanță IT de bază
    - Training inițial
    - Suport email
    - Ideal pentru IMM-uri mici
    """)

with col2:
    st.markdown("""
    **Pachet PROFESIONAL** (1500 - 2500 lei/lună)
    - Consultanță IT + Software
    - Analiză date
    - Suport prioritar
    - Ideal pentru IMM-uri medii
    """)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Pachet ENTERPRISE** (3000+ lei/lună)
    - Toate serviciile
    - Dedicare echipă
    - Suport 24/7
    - Ideal pentru IMM-uri mari
    """)

with col2:
    st.markdown("""
    **Pachet CUSTOM**
    - Complet personalizat
    - După nevoile tale
    - Preț negociabil
    - Contactează-ne pentru detalii
    """)

st.markdown("---")

# De ce să alegeți S_FLOW
st.subheader("✅ De Ce Să Ne Alegeți")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    **Profesionalism**
    - Echipă dedicată
    - Experiență de 3+ ani
    - Clienți satisfăcuți
    """)

with col2:
    st.info("""
    **Flexibilitate**
    - Prețuri competitive
    - Contracte flexibile
    - Soluții adaptate
    """)

with col3:
    st.warning("""
    **Calitate**
    - Conformitate GDPR
    - Certificări ISO
    - Garanții servicii
    """)

st.markdown("---")

# Proces de lucru
st.subheader("🔄 Procesul Nostru de Lucru")

steps = {
    "1️⃣ Consultație": "Analizez nevoile și obiectivele tale",
    "2️⃣ Ofertă": "Te prezint o propunere personalizată",
    "3️⃣ Contract": "Semnez documentele și convinurile",
    "4️⃣ Implementare": "Lucrez la soluția ta",
    "5️⃣ Training": "Instruiesc echipa ta",
    "6️⃣ Suport": "Oferim asistență continuă"
}

col1, col2, col3 = st.columns(3)

for i, (step, desc) in enumerate(steps.items()):
    if i % 3 == 0:
        col = col1
    elif i % 3 == 1:
        col = col2
    else:
        col = col3
    
    with col:
        st.markdown(f"""
        **{step}**
        
        {desc}
        """)

st.markdown("---")

# CTA
st.subheader("🚀 Gata Să Începi?")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Cere o Consultație Gratuită", use_container_width=True):
        st.switch_page("pages/5_💼_Contact.py")

with col2:
    if st.button("👥 Vezi Clienții Noștri", use_container_width=True):
        st.switch_page("pages/3_👥_Clienti.py")

with col3:
    if st.button("⭐ Citește Recenziile", use_container_width=True):
        st.switch_page("pages/6_⭐_Recenzii.py")

st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px; margin-top: 40px;">
    <p>Preț personaliza după complexitate și durata proiectului</p>
    <p>Contactează-ne pentru o ofertă fără obligații</p>
</div>
""", unsafe_allow_html=True)