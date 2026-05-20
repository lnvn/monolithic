from fastapi import FastAPI

app = FastAPI(title="E-Commerce")

@app.get("/")
def health_check():
    return {"status": "ok"}