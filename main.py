import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from apps.api.controllers.country_controller import country_router
from infra.database.database_connection import engine


def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="Meczownik Backend")

app.include_router(country_router, tags=["country"])

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        ssl_keyfile="./utils/certificates/key.pem",
        ssl_certfile="./utils/certificates/cert.pem"
    )
@app.get("/")
def health_check():
    return "Service is running."