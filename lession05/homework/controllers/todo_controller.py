from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from dependencies.db import get_db
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.base import SuccessResponse
from schemas.response.error_response import ErrorResponse
from schemas.response.todo_out_schema import TodoOut
from services import todo_service
from services.todo_service import TodoService

todo_router = APIRouter()
service = TodoService()

@todo_router.get("",response_model=SuccessResponse[list[TodoOut]])
def list_todos(
    offset: int = 0,
    limit: int = 100,
        db: Session = Depends(get_db)
) -> SuccessResponse[list[TodoOut]]:
    todos = service.list_todos(db, offset, limit)
    data = [TodoOut.model_validate(todo) for todo in todos]
    return SuccessResponse(data=data)

@todo_router.post(
    "",
    response_model=SuccessResponse[TodoOut],
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Business validation error"},
        409: {"model": ErrorResponse, "description": "Title already exists"}
    }
)
def create_todo(
        data: TodoCreate,
        response: Response,
        db: Session = Depends(get_db)
) -> SuccessResponse[TodoOut]:
    todo = service.create_todo(db, data)

    response.headers["location"] = f"/todos/{todo.id}"

    return SuccessResponse(data=TodoOut.model_validate(todo))

@todo_router.get(
    "/{todo_id:int}",
    response_model=SuccessResponse[TodoOut],
    responses={404: {"model": ErrorResponse, "description": "Todo not found"}}
)
def get_todo(
        todo_id: int,
        db: Session = Depends(get_db),
) -> SuccessResponse[TodoOut]:
    todo = service.get_todo(db, todo_id)
    return SuccessResponse(data=TodoOut.model_validate(todo))

@todo_router.get(
    "/search",
    response_model=SuccessResponse[list[TodoOut]],
    responses={400: {"model": ErrorResponse, "description": "Invalid search parameters (business rule violation)"}}
)
def search_todo(
        keyword: str | None = None,
        done: bool | None = None,
        offset: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
) -> SuccessResponse[list[TodoOut]]:
    todos = service.search_todos(
        db,
        keyword=keyword,
        done=done,
        offset=offset,
        limit=limit
    )
    data = [TodoOut.model_validate(todo) for todo in todos]
    return SuccessResponse(data=data)

@todo_router.patch(
    "/{todo_id:int}",
    response_model=SuccessResponse[TodoOut],
    responses={
        400: {"model": ErrorResponse, "description": "Business validation error"},
        404: {"model": ErrorResponse, "description": "Not found"},
    }
)
def update_todo_patch(
        todo_id: int,
        data: TodoUpdate,
        db: Session = Depends(get_db)
) -> SuccessResponse[TodoOut]:
    todo = service.update_todo_patch(db, todo_id, data)
    return SuccessResponse(data=TodoOut.model_validate(todo))

@todo_router.put(
"/{todo_id:int}",
    response_model=SuccessResponse[TodoOut],
    responses={
        400: {"model": ErrorResponse, "description": "Business validation error"},
        404: {"model": ErrorResponse, "description": "Not found"},
    }
)
def update_to_put(
        todo_id: int,
        data: TodoCreate,
        db: Session = Depends(get_db)
) -> SuccessResponse[TodoOut]:
    todo = service.update_todo_put(db, todo_id, data)
    return SuccessResponse(data=TodoOut.model_validate(todo))

@todo_router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse, "description": "Not found"}}
)
def delete_todo(
        todo_id: int,
        db: Session = Depends(get_db)
) -> None:
    service.delete_todo(db, todo_id)
    return None


