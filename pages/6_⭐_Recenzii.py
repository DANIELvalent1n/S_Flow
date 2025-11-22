# pages/6_⭐_Recenzii.py

import streamlit as st
from modules.database import Database
from modules.utils import display_success_message, display_error_message, validate_email
import pandas as pd

st.set_page_config(page_title="Recenzii - S_FLOW", layout="wide")

st.title("⭐ Recenzii și Feedback")
st.markdown("Citeste ce spun clienții noștri despre serviciile S_FLOW")

st.markdown("---")

db = Database()

# Tabs
tab1, tab2, tab3 = st.tabs(["⭐ Publică Recenzie", "📋 Recenzii Clienți", "📊 Statistici"])

with tab1:
    st.subheader("Lasă o Recenzie")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        Opiniile tale ne ajută să ne îmbunătățim serviciile.
        Apreciem feedback-ul sincer și constructiv!
        """)
    
    with col2:
        st.info("""
        **Recenziile tale vor fi:**
        - Moderate pentru calitate
        - Publicate pe site-ul nostru
        - Protejate confidențial
        """)
    
    with st.form("review_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            client_name = st.text_input("👤 Nume (Persoană/Firmă) *")
            email = st.text_input("📧 Email *")
        
        with col2:
            company = st.text_input("🏢 Compania (opțional)")
            rating = st.select_slider(
                "⭐ Rating",
                options=[1, 2, 3, 4, 5],
                value=5,
                format_func=lambda x: "⭐" * x
            )
        
        comment = st.text_area("💬 Comentariu *", height=120)
        
        consent = st.checkbox("Autorizez publicarea recenziei mele pe site-ul S_FLOW *")
        
        submitted = st.form_submit_button("✅ Publică Recenzie", use_container_width=True)
        
        if submitted:
            errors = []
            
            if not client_name or client_name.strip() == "":
                errors.append("Completează numele!")
            if not email or email.strip() == "":
                errors.append("Completează email!")
            elif not validate_email(email):
                errors.append("Email invalid!")
            if not comment or comment.strip() == "":
                errors.append("Completează comentariul!")
            if not consent:
                errors.append("Trebuie să autorizezi publicarea recenziei!")
            
            if errors:
                for error in errors:
                    display_error_message(error)
            else:
                if db.add_testimonial(client_name, company, email, rating, comment):
                    display_success_message("Mulțumim pentru recenzie! Va fi publicată după moderare.")
                    st.balloons()
                else:
                    display_error_message("Eroare la salvarea recenziei.")

with tab2:
    st.subheader("📋 Recenzii Clienți")
    
    df_reviews = db.get_all_testimonials()
    
    if not df_reviews.empty:
        # Filtre
        col1, col2 = st.columns(2)
        
        with col1:
            sort_by = st.selectbox("Sortează după", ["Cel mai recent", "Rating (descrescător)", "Rating (crescător)"])
        
        with col2:
            filter_rating = st.multiselect(
                "Filtrează după rating",
                [5, 4, 3, 2, 1],
                default=[5, 4, 3, 2, 1],
                format_func=lambda x: "⭐" * x
            )
        
        # Aplicare filtre
        df_filtered = df_reviews[df_reviews['rating'].isin(filter_rating)]
        
        # Sortare
        if sort_by == "Cel mai recent":
            df_filtered = df_filtered.sort_values('created_at', ascending=False)
        elif sort_by == "Rating (descrescător)":
            df_filtered = df_filtered.sort_values('rating', ascending=False)
        else:
            df_filtered = df_filtered.sort_values('rating', ascending=True)
        
        st.markdown(f"**Total: {len(df_filtered)} recenzii**")
        st.markdown("---")
        
        # Afișare recenzii
        for idx, review in df_filtered.iterrows():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                # Header recenzie
                st.write(f"**{review['client_name']}** {f'- {review["company"]}' if review['company'] else ''}")
                
                # Rating
                st.write(f"{'⭐' * review['rating']} ({review['rating']}/5)")
                
                # Comentariu
                st.write(f"*{review['comment']}*")
            
            with col2:
                if review['created_at']:
                    from modules.utils import days_since
                    days = days_since(review['created_at'])
                    if days == 0:
                        st.caption("📆 Astazi")
                    elif days == 1:
                        st.caption("📆 Ieri")
                    else:
                        st.caption(f"📆 {days} zile")
            
            st.divider()
    else:
        st.info("📭 Nu sunt recenzii inca. Fii prima persoană care lasă o recenzie!")

with tab3:
    st.subheader("📊 Statistici Recenzii")
    
    df_reviews = db.get_all_testimonials()
    
    if not df_reviews.empty:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Recenzii", len(df_reviews))
        
        with col2:
            avg_rating = df_reviews['rating'].mean()
            st.metric("Rating Mediu", f"{avg_rating:.1f}/5")
        
        with col3:
            five_star = len(df_reviews[df_reviews['rating'] == 5])
            st.metric("5 Stele", five_star)
        
        with col4:
            latest_date = df_reviews['created_at'].max()
            st.caption(f"Ultima recenzie: {latest_date}")
        
        st.markdown("---")
        
        # Distribuție rating-uri
        try:
            import plotly.express as px
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Distribuție Rating-uri")
                rating_counts = df_reviews['rating'].value_counts().sort_index(ascending=False)
                fig = px.bar(
                    x=rating_counts.index,
                    y=rating_counts.values,
                    labels={'x': 'Rating', 'y': 'Număr Recenzii'},
                    title="Recenzii pe Rating"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Breakdown Rating-uri")
                for rating in range(5, 0, -1):
                    count = len(df_reviews[df_reviews['rating'] == rating])
                    percentage = (count / len(df_reviews)) * 100
                    st.write(f"{'⭐' * rating} - {count} recenzii ({percentage:.1f}%)")
        
        except Exception as e:
            st.error(f"Eroare la generarea graficelor: {e}")
        
        st.markdown("---")
        
        # Mostru recenzii 5 stele
        st.subheader("🌟 Recenzii cu 5 Stele")
        
        five_star_reviews = df_reviews[df_reviews['rating'] == 5].sort_values('created_at', ascending=False).head(3)
        
        if not five_star_reviews.empty:
            for idx, review in five_star_reviews.iterrows():
                st.success(f"""
                **{review['client_name']}** - {review['company'] if review['company'] else 'N/A'}
                
                ⭐⭐⭐⭐⭐
                
                "{review['comment']}"
                """)
                st.divider()
        else:
            st.info("Nu sunt recenzii cu 5 stele inca.")
    else:
        st.info("📭 Nu sunt recenzii pentru a afișa statistici.")
