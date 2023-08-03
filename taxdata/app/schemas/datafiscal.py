"""
Script manages Schemas
"""
from datetime import datetime, date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, validator

def convert_datetime_to_iso_8601_with_z_suffix(dt: datetime) -> str:
    return dt.strftime('%d-%m-%Y')


class GenderEnum(str, Enum):
    women = "Mujer"
    man = "Hombre"


class RfcSchema(BaseModel):
    """
    Class Rfc Schema 
    """
    name: str
    last_name: str
    mother_last_name: Optional[str] = None
    birth_date: date


class CurpSchema(BaseModel):
    """
    Class Curp Schema 
    """
    name: str
    last_name: str
    mother_last_name: Optional[str] = None
    birth_date: date
    gender: GenderEnum
    state: str

    # @validator("birth_date", pre=True)
    # def parse_birthdate(cls, value):
    #     return datetime.strptime(
    #         value,
    #         "%Y-%m-%d"
    #     ).date()

    class Config:
        json_encoders = {datetime: lambda dt: dt.isoformat()}
        datetime_parse_format = "%d-%m-%Y"


class NssSchema(BaseModel):
    """
    Class Nss Schema 
    """
    nss: int
