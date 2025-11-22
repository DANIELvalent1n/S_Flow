# modules/database.py - Gestionare bază de date SQLite

import sqlite3
import pandas as pd
from datetime import datetime
from config import DATABASE_PATH
import streamlit as st

class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Returnează conexiune la baza de date"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            conn.row_factory = sqlite3.Row
            return conn
        except Exception as e:
            st.error(f"❌ Eroare conexiune bază de date: {e}")
            return None
    
    def init_database(self):
        """Inițializează baza de date cu toate tabelele necesare"""
        conn = self.get_connection()
        if not conn:
            return
        
        cursor = conn.cursor()
        
        try:
            # Tabel Clienți
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_name TEXT NOT NULL,
                    contact_name TEXT,
                    email TEXT,
                    phone TEXT,
                    service_type TEXT,
                    monthly_budget REAL,
                    status TEXT,
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabel Proiecte
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    service TEXT,
                    status TEXT,
                    start_date DATE,
                    end_date DATE,
                    budget REAL,
                    progress INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
                )
            ''')
            
            # Tabel Contacte
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contact_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    company TEXT,
                    phone TEXT,
                    subject TEXT,
                    message TEXT NOT NULL,
                    status TEXT DEFAULT 'Noi',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabel Recenzii
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS testimonials (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    company TEXT,
                    email TEXT,
                    rating INTEGER,
                    comment TEXT,
                    approved INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabel Servicii
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS services_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER,
                    service_type TEXT,
                    description TEXT,
                    date_service DATE,
                    duration_hours REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients(id)
                )
            ''')
            
            # Tabel Facturi
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS invoices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    project_id INTEGER,
                    invoice_number TEXT UNIQUE,
                    amount REAL,
                    status TEXT DEFAULT 'Neexpediată',
                    issue_date DATE,
                    due_date DATE,
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients(id),
                    FOREIGN KEY (project_id) REFERENCES projects(id)
                )
            ''')
            
            conn.commit()
            
        except Exception as e:
            st.error(f"❌ Eroare inițializare bază de date: {e}")
        finally:
            conn.close()
    
    # OPERAȚII CLIENȚI
    
    def add_client(self, company_name, contact_name, email, phone, service_type, monthly_budget, status, notes=""):
        """Adaugă un client nou"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clients 
                (company_name, contact_name, email, phone, service_type, monthly_budget, status, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (company_name, contact_name, email, phone, service_type, monthly_budget, status, notes))
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare adăugare client: {e}")
            return False
        finally:
            conn.close()
    
    def get_all_clients(self):
        """Returnează toți clienții"""
        query = "SELECT * FROM clients ORDER BY created_at DESC"
        try:
            return pd.read_sql_query(query, sqlite3.connect(str(self.db_path)))
        except Exception as e:
            st.error(f"❌ Eroare încărcare clienți: {e}")
            return pd.DataFrame()
    
    def get_client_by_id(self, client_id):
        """Returnează un client după ID"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
            return cursor.fetchone()
        except Exception as e:
            st.error(f"❌ Eroare: {e}")
            return None
        finally:
            conn.close()
    
    def update_client(self, client_id, **kwargs):
        """Actualizează datele unui client"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            columns = ", ".join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values()) + [client_id]
            
            cursor = conn.cursor()
            cursor.execute(f"UPDATE clients SET {columns}, updated_at = CURRENT_TIMESTAMP WHERE id = ?", values)
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare actualizare client: {e}")
            return False
        finally:
            conn.close()
    
    def delete_client(self, client_id):
        """Șterge un client"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare ștergere client: {e}")
            return False
        finally:
            conn.close()
    
    # OPERAȚII PROIECTE
    
    def add_project(self, client_id, project_name, description, service, status, start_date, end_date, budget):
        """Adaugă un proiect nou"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO projects 
                (client_id, project_name, description, service, status, start_date, end_date, budget)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (client_id, project_name, description, service, status, start_date, end_date, budget))
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare adăugare proiect: {e}")
            return False
        finally:
            conn.close()
    
    def get_all_projects(self):
        """Returnează toate proiectele cu datele clientului"""
        query = """
            SELECT p.*, c.company_name 
            FROM projects p
            JOIN clients c ON p.client_id = c.id
            ORDER BY p.start_date DESC
        """
        try:
            return pd.read_sql_query(query, sqlite3.connect(str(self.db_path)))
        except Exception as e:
            st.error(f"❌ Eroare încărcare proiecte: {e}")
            return pd.DataFrame()
    
    def get_projects_by_client(self, client_id):
        """Returnează proiectele unui client"""
        query = "SELECT * FROM projects WHERE client_id = ? ORDER BY start_date DESC"
        try:
            return pd.read_sql_query(query, sqlite3.connect(str(self.db_path)), params=[client_id])
        except Exception as e:
            st.error(f"❌ Eroare: {e}")
            return pd.DataFrame()
    
    def update_project(self, project_id, **kwargs):
        """Actualizează un proiect"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            columns = ", ".join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values()) + [project_id]
            
            cursor = conn.cursor()
            cursor.execute(f"UPDATE projects SET {columns}, updated_at = CURRENT_TIMESTAMP WHERE id = ?", values)
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare actualizare proiect: {e}")
            return False
        finally:
            conn.close()
    
    # OPERAȚII CONTACTE
    
    def add_contact_request(self, name, email, company, phone, subject, message):
        """Adaugă o solicitare de contact"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contact_requests 
                (name, email, company, phone, subject, message)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, email, company, phone, subject, message))
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare adăugare contact: {e}")
            return False
        finally:
            conn.close()
    
    def get_all_contact_requests(self):
        """Returnează toate solicitările de contact"""
        query = "SELECT * FROM contact_requests ORDER BY created_at DESC"
        try:
            return pd.read_sql_query(query, sqlite3.connect(str(self.db_path)))
        except Exception as e:
            st.error(f"❌ Eroare: {e}")
            return pd.DataFrame()
    
    # OPERAȚII RECENZII
    
    def add_testimonial(self, client_name, company, email, rating, comment):
        """Adaugă o recenzie"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO testimonials 
                (client_name, company, email, rating, comment)
                VALUES (?, ?, ?, ?, ?)
            ''', (client_name, company, email, rating, comment))
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"❌ Eroare adăugare recenzie: {e}")
            return False
        finally:
            conn.close()
    
    def get_all_testimonials(self, approved_only=False):
        """Returnează toate recenziile"""
        if approved_only:
            query = "SELECT * FROM testimonials WHERE approved = 1 ORDER BY created_at DESC"
        else:
            query = "SELECT * FROM testimonials ORDER BY created_at DESC"
        
        try:
            return pd.read_sql_query(query, sqlite3.connect(str(self.db_path)))
        except Exception as e:
            st.error(f"❌ Eroare: {e}")
            return pd.DataFrame()
    
    # STATISTICI
    
    def get_stats(self):
        """Returnează statistici generale"""
        conn = self.get_connection()
        if not conn:
            return {}
        
        try:
            cursor = conn.cursor()
            
            total_clients = cursor.execute("SELECT COUNT(*) FROM clients").fetchone()[0]
            active_clients = cursor.execute(
                "SELECT COUNT(*) FROM clients WHERE status = 'Client Activ'"
            ).fetchone()[0]
            total_projects = cursor.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
            completed_projects = cursor.execute(
                "SELECT COUNT(*) FROM projects WHERE status = 'Finalizat'"
            ).fetchone()[0]
            total_budget = cursor.execute(
                "SELECT COALESCE(SUM(monthly_budget), 0) FROM clients"
            ).fetchone()[0]
            avg_rating = cursor.execute(
                "SELECT COALESCE(AVG(rating), 0) FROM testimonials WHERE approved = 1"
            ).fetchone()[0]
            
            return {
                "total_clients": total_clients,
                "active_clients": active_clients,
                "total_projects": total_projects,
                "completed_projects": completed_projects,
                "total_budget": total_budget,
                "avg_rating": round(avg_rating, 1)
            }
        except Exception as e:
            st.error(f"❌ Eroare statistici: {e}")
            return {}
        finally:
            conn.close()