from fastapi import APIRouter

from views import logins_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(logins_view.router, prefix=logins_view.ENDPOINT_NAME)