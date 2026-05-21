from fastapi import FastAPI
from app.auth.router import router as auth_router

app = FastAPI(title="E-Commerce")

app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "ok"}