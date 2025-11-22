# modules/__init__.py

from .database import Database
from .models import Client, Project, ContactRequest, Testimonial, Service
from .utils import (
    format_currency,
    format_date,
    get_status_color,
    validate_email,
    validate_phone,
    get_progress_bar,
    display_success_message,
    display_error_message,
    display_info_message,
    display_warning_message
)

__all__ = [
    'Database',
    'Client',
    'Project',
    'ContactRequest',
    'Testimonial',
    'Service',
    'format_currency',
    'format_date',
    'get_status_color',
    'validate_email',
    'validate_phone',
    'get_progress_bar',
    'display_success_message',
    'display_error_message',
    'display_info_message',
    'display_warning_message'
]