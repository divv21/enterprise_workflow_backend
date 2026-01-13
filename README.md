# Enterprise Workflow Management Backend

A production-style backend service built using FastAPI, demonstrating role-based authentication, authorization, enterprise architecture patterns, and state-managed workflow operations.

## Features
- JWT authentication and password hashing (bcrypt)
- Role-based access: ADMIN vs USER
- Admin-controlled user provisioning
- Task lifecycle with controlled state transitions
- Layered architecture (routes → services → repository → models)

## Tech Stack
- FastAPI, Python
- SQLite + SQLAlchemy ORM
- OAuth2 + JWT
- Uvicorn ASGI

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## routes
* `/auth/login`
* `/auth/register`
* `/tasks/`
* `/tasks/{task_id}/status`
