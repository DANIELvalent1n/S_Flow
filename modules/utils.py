# modules/utils.py - Funcții utilitare

import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

def format_currency(value):
    """Formatează valoare ca monedă RON"""
    return f"{value:,.2f} lei".replace(",", ".")

def format_date(date_obj):
    """Formatează data în format citibil"""
    if isinstance(date_obj, str):
        return date_obj
    try:
        return date_obj.strftime("%d.%m.%Y")
    except:
        return str(date_obj)

def get_status_color(status):
    """Returnează culoare pentru status"""
    status_colors = {
        "Client Activ": "🟢",
        "Prospect": "🟡",
        "Client Inactiv": "🔴",
        "În Curs": "🔵",
        "Finalizat": "✅",
        "Planificare": "📋",
        "Suspendat": "⏸️",
        "Noi": "📨",
        "Răspuns": "✉️"
    }
    return status_colors.get(status, "⚪")

def get_progress_bar(progress):
    """Crează o bară de progres"""
    filled = int(progress / 10)
    return "█" * filled + "░" * (10 - filled) + f" {progress}%"

def validate_email(email):
    """Validează o adresă de email"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validează un număr de telefon"""
    import re
    pattern = r'^[\d\s\-\+\(\)]{7,}$'
    return re.match(pattern, phone) is not None

def get_date_range_stats(df, date_column, days=30):
    """Calculează statistici pentru o perioadă de zile"""
    if df.empty:
        return 0
    
    try:
        df[date_column] = pd.to_datetime(df[date_column])
        cutoff_date = datetime.now() - timedelta(days=days)
        return len(df[df[date_column] >= cutoff_date])
    except:
        return 0

def create_pie_chart_data(df, column):
    """Crează date pentru grafic pie"""
    if df.empty:
        return pd.DataFrame()
    return df[column].value_counts()

def create_bar_chart_data(df, x_col, y_col):
    """Crează date pentru grafic bar"""
    if df.empty:
        return pd.DataFrame()
    return df.groupby(x_col)[y_col].sum()

def display_success_message(message):
    """Afișează mesaj de succes"""
    st.success(f"✅ {message}")

def display_error_message(message):
    """Afișează mesaj de eroare"""
    st.error(f"❌ {message}")

def display_info_message(message):
    """Afișează mesaj informativ"""
    st.info(f"ℹ️ {message}")

def display_warning_message(message):
    """Afișează mesaj de avertisment"""
    st.warning(f"⚠️ {message}")

def get_service_icon(service_type):
    """Returnează icon pentru tip serviciu"""
    icons = {
        "Consultanță IT": "💼",
        "Dezvoltare Software": "🛠️",
        "Analiză Date": "📊",
        "Training": "🎓",
        "Altul": "❓"
    }
    return icons.get(service_type, "📌")

def days_since(date_string):
    """Calculează zilele trecute de la o dată"""
    try:
        date_obj = pd.to_datetime(date_string)
        return (datetime.now() - date_obj).days
    except:
        return None

def calculate_project_progress(start_date, end_date, current_status):
    """Calculează procentul de progres al unui proiect"""
    try:
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)
        now = datetime.now()
        
        if current_status == "Finalizat":
            return 100
        elif current_status == "Planificare":
            return 0
        elif current_status == "Suspendat":
            return 50
        else:  # În Curs
            total_days = (end - start).days
            elapsed_days = (now - start).days
            if total_days <= 0:
                return 0
            progress = min(int((elapsed_days / total_days) * 100), 99)
            return max(progress, 0)
    except:
        return 0

def highlight_html(text, color="yellow"):
    """Crează text colorat în HTML"""
    colors = {
        "yellow": "#FFFF00",
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF"
    }
    hex_color = colors.get(color, color)
    return f'<span style="background-color: {hex_color}; padding: 2px;">{text}</span>'