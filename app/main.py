from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, task
from app.routes import auth, register, task
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi import Request
from app.core.exceptions import http_error_handler, generic_error_handler

app = FastAPI(
    title="Enterprise Workflow Management System",
    description ="Backend system for managing tasks with role-based access",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(register.router)
app.include_router(task.router)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, generic_error_handler)

@app.get("/health")
def health_check():
    return {"status": "OK"} 


