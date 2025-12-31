from sqlalchemy.orm import Session
from app.repository.user_repository import get_user_by_email
from app.core.security import verify_password, create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def generate_token(user):
    return create_access_token({"sub": user.email, "role": user.role})
