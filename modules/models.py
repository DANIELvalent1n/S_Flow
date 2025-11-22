# modules/models.py - Modele de date

from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

@dataclass
class Client:
    """Model pentru client"""
    company_name: str
    contact_name: str
    email: str
    phone: str
    service_type: str
    monthly_budget: float
    status: str
    notes: str = ""
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Project:
    """Model pentru proiect"""
    client_id: int
    project_name: str
    description: str
    service: str
    status: str
    start_date: date
    end_date: date
    budget: float
    progress: int = 0
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class ContactRequest:
    """Model pentru solicitare de contact"""
    name: str
    email: str
    message: str
    company: Optional[str] = None
    phone: Optional[str] = None
    subject: Optional[str] = None
    id: Optional[int] = None
    status: str = "Noi"
    created_at: Optional[datetime] = None

@dataclass
class Testimonial:
    """Model pentru recenzie"""
    client_name: str
    rating: int
    comment: str
    company: Optional[str] = None
    email: Optional[str] = None
    approved: bool = False
    id: Optional[int] = None
    created_at: Optional[datetime] = None

@dataclass
class Service:
    """Model pentru serviciu"""
    id: int
    name: str
    price_min: float
    price_max: float
    unit: str
    description: str
    features: list