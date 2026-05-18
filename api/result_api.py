from fastapi import APIRouter

from services.result_service import ResultService
from repositories.inmemory.in_memory_result_repository import InMemoryResultRepository
from src.result import Result

router = APIRouter()

repo = InMemoryResultRepository()

service = ResultService(repo)


@router.get("/api/results")
def get_results():

    return service.get_all_results()


@router.post("/api/results")
def create_result():

    result = Result("1", 90, "Fake")

    service.create_result(result)

    return {"message": "Result created"}


@router.put("/api/results/{result_id}")
def update_result(result_id: str):

    updated_result = Result(result_id, 95, "Real")

    service.update_result(result_id, updated_result)

    return {"message": "Result updated"}


@router.delete("/api/results/{result_id}")
def delete_result(result_id: str):

    service.delete_result(result_id)

    return {"message": "Result deleted"}