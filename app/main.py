from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, task
from app.routes import auth

app = FastAPI(
    title="Enterprise Workflow Management System",
    description ="Backend system for managing tasks with role-based access",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "OK"} 


