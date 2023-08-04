"""
Script that manages the date utilities.
"""
from datetime import datetime


def convert_datetime_to_str(dt: datetime) -> str:
    return dt.strftime('%d-%m-%Y')
