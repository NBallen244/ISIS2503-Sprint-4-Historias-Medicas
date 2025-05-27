# Models for the places microservice

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId


class Rol(str, Enum):
    Medico = "medico"
    Medica = "medica"
    Enfermera = "enfermera"
    Enfermero = "enfermero"
    Hacker= "hackerspace"


class Login(BaseModel):
    nombre: str = Field(...)
    correo: str = Field(...)
    contraseña: str = Field(...)
    rol: Rol = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "nombre": "Mauricio Linares",
                "correo": "m.vistasbellas@ggmail.com",
                "contraseña": "helloworld",
                "rol": Rol.Medico,
            }
        },
    )


class LoginOut(Login):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "nombre": "Mauricio Linares",
                "correo": "m.vistasbellas@ggmail.com",
                "contraseña": "helloworld",
                "rol": Rol.Medico,
            }
        },
    )


class LoginCollection(BaseModel):
    # A collection of places
    logins: List[LoginOut] = Field(...)
