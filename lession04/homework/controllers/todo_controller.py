from fastapi import APIRouter
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.error_response import ErrorResponse
from schemas.response.todo_out_schema import TodoOut
from services import todo_service

todo_router = APIRouter()

@todo_router.post(
    "",
    status_code=201,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid input or business logic"},
        409: {"model": ErrorResponse, "description": "Todo title already exists"}
    },
)
def create_todo(todo: TodoCreate) -> TodoOut:
    return todo_service.create_todo(todo)


@todo_router.get(
    "",
    response_model=list[TodoOut],
    status_code=200,
)
def get_all_todos(
    done: bool | None = None, keyword: str | None = None, limit: int = 10
) -> list[TodoOut]:
    return todo_service.get_all_todos(done, keyword, limit)


@todo_router.get(
    "/{id}",
    response_model=TodoOut,
    status_code=200,
    responses={
        404: {"model": ErrorResponse, "description": "Todo not found"}
    }
)
def get_todo_by_id(id: int) -> TodoOut:
    return todo_service.get_todo_by_id(id)

@todo_router.put(
    "/{id}",
    response_model=TodoOut,
    responses={
        404: {"model": ErrorResponse, "description": "Todo not found"},
        409: {"model": ErrorResponse, "description": "Todo title already exists"}
    }
)
def put_todo(id: int, todo: TodoCreate) -> TodoOut:
    return todo_service.put_todo(id, todo)

@todo_router.patch(
"/{id}",
    response_model=TodoOut,
    responses={
        404: {"model": ErrorResponse, "description": "Todo not found"},
        409: {"model": ErrorResponse, "description": "Todo title already exists"}
    }
)
def patch_todo(id: int, todo: TodoUpdate) -> TodoOut:
    return todo_service.patch_todo(id, todo)

@todo_router.delete(
    "/{id}",
    status_code=204,
    responses={
        404: {"model": ErrorResponse, "description": "Todo not found"}
    }
)
def delete_todo(id: int) -> None:
    todo_service.delete_todo(id)
