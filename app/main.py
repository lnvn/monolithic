from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.products.router import router as products_router

app = FastAPI(title="E-Commerce")

app.include_router(auth_router)
app.include_router(products_router)

@app.get("/")
def health_check():
    return {"status": "ok"}