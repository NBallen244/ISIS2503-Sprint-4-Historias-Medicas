from fastapi import APIRouter, status, Body
import logic.logins_logic as logins_service
from models.models import Login, LoginOut, LoginCollection

router = APIRouter()
ENDPOINT_NAME = "/logins"


@router.get(
    "/",
    response_description="List all logins",
    response_model=LoginCollection,
    status_code=status.HTTP_200_OK,
)
async def get_logins():
    return await logins_service.get_logins()


@router.get(
    "/{login_code}",
    response_description="Get a single login by its code",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def get_login(login_code: str):
    return await logins_service.get_login(login_code)

@router.get(
    "/logIn",
    response_description="Log In",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def login(login: Login = Body(...)):
    return await logins_service.logIn(login)

@router.get(
    "/clogin",
    response_description="Get current logged user info",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def get_loginActual(login_code: str):
    return await logins_service.getLoginActual()

@router.get(
    "/logout",
    response_description="Logs out current user",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def get_login(login_code: str):
    return await logins_service.logOut()

@router.post(
    "/",
    response_description="Create a new login",
    response_model=LoginOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_login(login: Login = Body(...)):
    return await logins_service.create_login(login)


@router.put(
    "/{login_code}",
    response_description="Update a login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def update_login(login_code: str, login: Login = Body(...)):
    return await logins_service.update_login(login_code, login)


@router.delete(
    "/{login_code}",
    response_description="Delete a login",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_login(login_code: str):
    return await logins_service.delete_login(login_code)
