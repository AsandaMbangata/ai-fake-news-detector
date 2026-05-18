from fastapi import APIRouter

from services.user_service import UserService
from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from src.user import User

router = APIRouter()

repo = InMemoryUserRepository()

service = UserService(repo)

@router.get("/api/users")
def get_users():
    return service.get_all_users()


@router.post("/api/users")
def create_user():
    user = User("1", "Kelly", "Admin")
    service.create_user(user)
    return {"message": "User created"}

@router.put("/api/users/{user_id}")
def update_user(user_id: str):
    updated_user = User(user_id, "Updated User", "Admin")
    service.update_user(user_id, updated_user)
    return {"message": "User updated"}


@router.delete("/api/users/{user_id}")
def delete_user(user_id: str):
    service.delete_user(user_id)
    return {"message": "User deleted"}