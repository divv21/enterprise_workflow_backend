from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdateStatus
from app.services.task_service import (
    create_task_service,
    get_user_id,
    update_status_service,
    get_all_tasks,
    get_user_tasks
)
from app.core.security import get_current_user, require_admin

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", dependencies=[Depends(require_admin)])
def create_task_route(
    data: TaskCreate,
    db: Session = Depends(get_db)
):
    task = create_task_service(db, data, admin=True)
    return {"message": "Task created", "task_id": task.id}

@router.get("/")
def list_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] == "ADMIN":
        return get_all_tasks(db)
    return get_user_tasks(db, get_user_id(db, user))

@router.patch("/{task_id}/status")
def update_status(
    task_id: int,
    data: TaskUpdateStatus,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    task = update_status_service(db, task_id, data.status, user)
    return {"message": "Task updated", "new_status": task.status}
