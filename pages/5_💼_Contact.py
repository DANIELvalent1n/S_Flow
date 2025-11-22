# pages/5_💼_Contact.py

import streamlit as st
from modules.database import Database
from modules.utils import validate_email, display_success_message, display_error_message
from config import COMPANY_INFO

st.set_page_config(page_title="Contact - S_FLOW", layout="wide")

st.title("💼 Contactează-ne")
st.markdown("Suntem aici pentru a-ți ajuta. Completează formularul și te vom contacta în curând.")

st.markdown("---")

db = Database()

col1, col2 = st.columns([1.5, 1])

# Formular contact
with col1:
    st.subheader("📧 Trimite-ne un Mesaj")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("👤 Nume Complet *")
        
        email = st.text_input("📧 Email *")
        
        company = st.text_input("🏢 Nume Firmă")
        
        phone = st.text_input("📞 Telefon")
        
        subject = st.selectbox("📌 Subiect", [
            "Ofertă servicii",
            "Informații suplimentare",
            "Partner colaborare",
            "Suport tehnic",
            "Altceva"
        ])
        
        message = st.text_area("💬 Mesajul Tău *", height=150)
        
        col1_form, col2_form = st.columns(2)
        
        with col1_form:
            newsletter = st.checkbox("Doresc să primesc newsletter-ul S_FLOW")
        
        with col2_form:
            terms = st.checkbox("Am citit și accept Termenii de Utilizare *")
        
        submitted = st.form_submit_button("📤 Trimite Mesaj", use_container_width=True)
        
        if submitted:
            # Validări
            errors = []
            
            if not name or name.strip() == "":
                errors.append("Completează nume complet!")
            if not email or email.strip() == "":
                errors.append("Completează email!")
            elif not validate_email(email):
                errors.append("Email invalid!")
            if not message or message.strip() == "":
                errors.append("Completează mesajul!")
            if not terms:
                errors.append("Trebuie să accepți termenii de utilizare!")
            
            if errors:
                for error in errors:
                    display_error_message(error)
            else:
                # Salvare în baza de date
                if db.add_contact_request(name, email, company, phone, subject, message):
                    display_success_message("Mesajul a fost trimis cu succes!")
                    st.balloons()
                    st.markdown("---")
                    st.success("✅ Te vom contacta în curând. Mulțumim!")
                else:
                    display_error_message("Eroare la trimiterea mesajului. Încearcă din nou.")

# Informații contact
with col2:
    st.subheader("📞 Informații Contact")
    
    st.markdown(f"""
    **S_FLOW**
    
    Consultanță IT & Digitalizare
    """)
    
    st.info(f"""
    📍 **Locație:**
    {COMPANY_INFO['location']}
    
    📧 **Email:**
    {COMPANY_INFO['email']}
    
    📞 **Telefon:**
    {COMPANY_INFO['phone']}
    
    🕐 **Orari Lucru:**
    {COMPANY_INFO['working_hours']}
    """)
    
    st.markdown("---")
    
    st.subheader("🗺️ Zone Acoperite")
    for zone in COMPANY_INFO['covered_zones']:
        st.write(f"• {zone}")
    
    st.markdown("---")
    
    st.subheader("💬 Rețele Sociale")
    col_fb, col_in, col_tw = st.columns(3)
    
    with col_fb:
        st.write("[🔵 Facebook](https://facebook.com)")
    
    with col_in:
        st.write("[📱 LinkedIn](https://linkedin.com)")
    
    with col_tw:
        st.write("[🐦 Twitter](https://twitter.com)")

st.markdown("---")

# Secție FAQ
st.subheader("❓ Întrebări Frecvente")

with st.expander("📌 Care este cel mai bun mod de a vă contacta?"):
    st.write("""
    Poți trimite un mesaj prin formularul de contact, ne poți suna sau ne poți trimite un email.
    Vei primi răspuns în maxim 24 de ore în zilele lucrătoare.
    """)

with st.expander("💰 Cum se stabilesc prețurile?"):
    st.write("""
    Prețurile se stabilesc în funcție de:
    - Complexitatea serviciului
    - Durata proiectului
    - Numărul de utilizatori
    - Nivel de personalizare
    
    Oferim o consultație gratuită pentru a determina prețul exact.
    """)

with st.expander("🔒 Sunt datele mele sigure?"):
    st.write("""
    Da! Respectăm pe deplin GDPR și protejăm datele clienților cu cea mai înaltă prioritate.
    Toate comunicațiile și datele sunt criptate și protejate.
    """)

with st.expander("⏱️ Care este durata unui proiect?"):
    st.write("""
    Durata variază în funcție de complexitate:
    - Consultanță: 2-4 săptămâni
    - Dezvoltare Software: 3-6 luni
    - Analiză Date: 2-3 săptămâni
    - Training: 1-2 săptămâni
    """)

with st.expander("🤝 Oferiți suport post-implementare?"):
    st.write("""
    Da! Oferi suport complet după implementare, inclusiv:
    - Suport tehnic 24/7
    - Update-uri regulate
    - Training angajați
    - Consultanță continuă
    """)

st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px; margin-top: 40px;">
    <p><strong>Așteptam cu nerăbdare să lucrăm cu tine!</strong></p>
    <p>© 2025 S_FLOW - Transformăm ideile în soluții digitale</p>
</div>
""", unsafe_allow_html=True)