from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.task_repository import (
    create_task, get_task_by_id, get_user_tasks,
    get_all_tasks, update_task_status
)
from app.repository.user_repository import get_user_by_email

VALID_TRANSITIONS = {
    "TODO": ["IN_PROGRESS"],
    "IN_PROGRESS": ["DONE"],
    "DONE": []
}

def create_task_service(db: Session, data, admin):
    return create_task(db, data.title, data.description, data.assigned_to)

def update_status_service(db: Session, task_id: int, new_status: str, user):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if user["role"] != "ADMIN" and task.assigned_to != get_user_id(db, user):
        raise HTTPException(status_code=403, detail="Not your task")

    if new_status not in VALID_TRANSITIONS.get(task.status, []):
        raise HTTPException(status_code=400, detail=f"Invalid transition from {task.status}")

    return update_task_status(db, task, new_status)

def get_user_id(db: Session, user):
    db_user = get_user_by_email(db, user["sub"])
    return db_user.id
