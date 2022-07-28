from fastapi import FastAPI
from router.base import router as router_user
from router.admin.product import router as router_admin_product
app = FastAPI()
app.include_router(router_user)
app.include_router(router_admin_product)
