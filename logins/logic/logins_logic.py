"""
This module contains the logic for the logins app.
Main functions:
- get_logins: Get a list of all logins
- get_login: Get a single login
- create_login: Create a new login
- update_login: Update a login
- delete_login: Delete a login
"""

from models.models import Login, LoginCollection
from models.db import logins_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

loginActual= None  # Placeholder for the current login context, if needed
codigoLoginActual = None  # Placeholder for the current login code context, if needed

async def get_logins():
    """
    Get a list of users
    :return: A list of users
    """
    logins = await logins_collection.find().to_list(1000)
    return LoginCollection(logins=logins)

async def logIn(login: Login):
    """
    Checks the login credentials and returns the user information if successful.
    :return: Logged user information
    """
    correo = login.correo
    contraseña = login.contraseña
    
    if (loginA := await logins_collection.find_one({"correo": correo, "contraseña": contraseña})) is not None:
        loginActual = loginA
        codigoLoginActual = loginA.get("code", None)
        return loginA

    raise HTTPException(
        status_code=404, detail=f"Correo y/o contraseña incorrectos"
    )
async def getLoginActual():
    """
    Get the current login information.
    :return: The current login information
    """
    if loginActual is not None:
        return loginActual
    elif codigoLoginActual is not None:
        if (login := await logins_collection.find_one({"code": codigoLoginActual})) is not None:
            return login

    raise HTTPException(
        status_code=404, detail="No hay usuario logueado actualmente"
    )
    
async def logOut():
    """
    Get a list of users
    :return: A list of users
    """
    loginActual= None
    codigoLoginActual = None
    return None

async def get_login(login_code: str):
    """
    Get a single login info / user info
    :param login_code: The code of the login
    :return: The login
    """
    if (login := await logins_collection.find_one({"code": login_code})) is not None:
        return login

    raise HTTPException(
        status_code=404, detail=f"Login with code {login_code} not found"
    )


async def create_login(login: Login):
    """
    Insert a new login record.
    """

    try:
        new_login = await logins_collection.insert_one(
            login.model_dump(by_alias=True, exclude=["id"])
        )
        created_login = await logins_collection.find_one({"_id": new_login.inserted_id})
        return created_login

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Login with code {login.code} already exists"
        )


async def update_login(login_code: str, login: Login):
    """
    Update a login
    :param login_code: The code of the login
    :param login: The login data
    :return: The updated login
    """

    try:
        update_result = await logins_collection.update_one(
            {"code": login_code},
            {"$set": login.model_dump(by_alias=True, exclude=["id"])},
        )
        if update_result.modified_count == 1:
            if (
                updated_login := await logins_collection.find_one({"code": login.code})
            ) is not None:
                return updated_login
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Place with code {login.code} already exists"
        )

    raise HTTPException(
        status_code=404,
        detail=f"Place with code {login_code} not found or no updates were made",
    )


async def delete_login(login_code: str):
    """
    Delete a login
    :param login_code: The code of the login
    """
    delete_result = await logins_collection.delete_one({"code": login_code})

    if delete_result.deleted_count == 1:
        return

    raise HTTPException(
        status_code=404, detail=f"Place with code {login_code} not found"
    )
