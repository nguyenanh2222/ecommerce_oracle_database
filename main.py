from fastapi import FastAPI
from router.base import router as router_user
app = FastAPI()
app.include_router(router_user)
