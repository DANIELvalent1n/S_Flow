# config.py - Configurații globale pentru S_FLOW

import os
from pathlib import Path

# Directoare
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

# Creare directoare dacă nu există
DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# Bază de date
DATABASE_PATH = DATA_DIR / "sflow.db"

# Informații firmă
COMPANY_INFO = {
    "name": "S_FLOW",
    "tagline": "Transformăm ideile în soluții digitale!",
    "description": """
    S_FLOW este o firmă de consultanță IT înființată în Timișoara, dedicată digitalizării 
    proceselor pentru IMM-uri. Ajutăm companiile să folosească tehnologia în mod simplu, 
    eficient și accesibil.
    """,
    "mission": """
    Să ajutăm firmele să înțeleagă și să folosească datele pentru a lua decizii mai bune, 
    oferind soluții IT simple și personalizate, chiar și pentru companiile fără experiență 
    tehnologică.
    """,
    "vision": """
    Să devenim una dintre cele mai apreciate firme de consultanță IT din vestul României, 
    recunoscută pentru abordare modernă și eficientă, oferind soluții inovative la prețuri accesibile.
    """,
    "location": "Timișoara, Timiș, România",
    "email": "contact@sflow.ro",
    "phone": "+40 (256) XXX-XXXX",
    "working_hours": "Luni - Vineri: 9:00 - 18:00",
    "covered_zones": ["Timiș", "Arad", "Bihor", "Cluj"],
    "founder_1": "Joldes Daniel Valentin",
    "founder_2": "Fati Georgiana - Luiza",
    "founder_3": "Bucos Adriana",
}

# Servicii
SERVICES = {
    "consultanta_it": {
        "id": 1,
        "name": "💼 Consultanță IT Personalizată",
        "price_min": 500,
        "price_max": 1500,
        "unit": "lei/lună",
        "description": "Analiza proceselor interne, optimizare și recomandări strategice pentru digitalizare.",
        "features": [
            "Audit complet al proceselor",
            "Identificare oportunități de optimizare",
            "Recomandări strategice",
            "Plan de implementare"
        ]
    },
    "software_dev": {
        "id": 2,
        "name": "🛠️ Dezvoltare Software Personalizată",
        "price_min": 1000,
        "price_max": 3000,
        "unit": "lei/lună",
        "description": "Aplicații cloud sau locale, adaptate nevoilor specifice ale afacerii tale.",
        "features": [
            "Aplicații web și desktop",
            "Soluții cloud",
            "Interfață intuitivă",
            "Suport post-implementare"
        ]
    },
    "data_analytics": {
        "id": 3,
        "name": "📊 Analiză și Raportare Date",
        "price_min": 800,
        "price_max": 2000,
        "unit": "lei/lună",
        "description": "Dashboard-uri vizuale și rapoarte care ajută la luarea deciziilor informate.",
        "features": [
            "Dashboard-uri personalizate",
            "Rapoarte automate",
            "Vizualizări de date",
            "Export în multiple formate"
        ]
    },
    "training_support": {
        "id": 4,
        "name": "🎓 Training și Suport Tehnic",
        "price_min": 600,
        "price_max": 1200,
        "unit": "lei/lună",
        "description": "Instruire angajați și asistență tehnică pentru soluțiile implementate.",
        "features": [
            "Training angajați",
            "Suport 24/7",
            "Documentație completă",
            "Update-uri regulate"
        ]
    }
}

# Servicii pe proiecte (pentru formular)
SERVICE_TYPES = ["Consultanță IT", "Dezvoltare Software", "Analiză Date", "Training", "Altul"]

# Statuts pentru clienți
CLIENT_STATUS = ["Prospect", "Client Activ", "Client Inactiv"]

# Statuts pentru proiecte
PROJECT_STATUS = ["Planificare", "În Curs", "Finalizat", "Suspendat"]

# Teme Streamlit
THEME_CONFIG = {
    "primary_color": "#1f77b4",
    "background_color": "#f5f7fa",
    "secondary_background_color": "#e8f1f8",
    "text_color": "#262730",
    "font": "sans serif"
}

# Obiective pe 3-5 ani
OBJECTIVES = [
    "Creșterea cifrei de afaceri cu 20% până la sfârșitul lui 2025",
    "Lansarea unei aplicații software noi până în 2026 și atragerea a cel puțin 3 clienți activi",
    "Extinderea echipei cu 30% între 2025 și 2026, inclusiv prin colaborări cu universități",
    "Obținerea unei certificări ISO până în 2026",
    "Reducerea timpului de implementare a proiectelor cu 15% până la sfârșitul lui 2025"
]

# Echipa
TEAM = {
    "manager_general": {
        "role": "Manager General",
        "salary": 10000,
        "description": "Conducerea firmei, strategie, parteneriate",
        "cor_code": "112029"
    },
    "manager_tehnic": {
        "role": "Manager Tehnic (CTO)",
        "salary": 9000,
        "description": "Coordonarea echipei IT, control calitate software",
        "cor_code": "133006"
    },
    "manager_operational": {
        "role": "Manager Operațional (COO)",
        "salary": 8000,
        "description": "Organizare proiecte, relații clienți",
        "cor_code": "121901"
    }
}

# Legislație aplicabilă
LEGISLATION = [
    "Legea nr. 31/1990 privind societățile comerciale",
    "Legea 506/2004 privind prelucrarea datelor personale",
    "Regulamentul GDPR (UE 2016/679)",
    "Legea 227/2015 - Codul Fiscal",
    "Legea securității cibernetice nr. 362/2018",
    "ISO/IEC 27001:2022 - Managementul securității informațiilor"
]

# Perspective de dezvoltare
DEVELOPMENT_PERSPECTIVES = {
    "3_years": "Recunoscuți în Timișoara și județele din jur pentru serviciile noastre cu portofoliu solid de clienți",
    "5_years": "Lansate aplicații software noi și recunoscuți pentru soluții eficiente și accesibile",
    "10_years": "Punct de referință în România pentru consultanță IT și digitalizarea IMM-urilor, poate și internațional"
}

# Piață țintă
MARKET_INFO = {
    "total_companies": "20.000-30.000",
    "region": "Vestul României (Timiș, Arad, Bihor, Cluj)",
    "target_segment": "IMM-uri cu 5-100 angajați",
    "client_budget_min": 500,
    "client_budget_max": 3000,
    "client_budget_unit": "lei/lună",
    "market_growth": "Creștere constantă datorită digitalizării obligatorii și GDPR"
}