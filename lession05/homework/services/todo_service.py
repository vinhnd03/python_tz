from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from repositories.todo_repository import TodoRepository
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from models import Todo

class TodoService:
    def __init__(self):
        self.repo = TodoRepository()

    def create_todo(self, db: Session, data: TodoCreate) -> Todo:
        existed = self.repo.get_by_title(db, str(data.title))
        if existed:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Title already exists"
            )
        if data.priority < 1 or data.priority > 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Priority must be >= 1 and <= 5",
            )

        todo = Todo(**data.model_dump())
        return self.repo.create(db, todo)

    def get_todo(self, db: Session, todo_id: int) -> Todo:
        todo = self.repo.get_by_id(db, todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )
        return todo

    def list_todos (self, db: Session, offset: int = 0, limit: int = 100) -> list[Todo]:
        return self.repo.list(db, offset=offset, limit=limit)

    def search_todos(
            self,
            db: Session,
            done: bool,
            keyword: str,
            offset: int = 0,
            limit: int = 100) -> list[Todo]:

        return self.repo.search(
            db,
            done=done,
            keyword=keyword,
            offset=offset,
            limit=limit
        )

    def update_todo_put(self, db: Session, todo_id: int, data: TodoCreate) -> Todo:
        todo = self.get_todo(db, todo_id)
        existed = self.repo.get_by_title(db, str(data.title))
        if existed and existed.id != todo_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Title already exists"
            )
        if data.priority < 1 or data.priority > 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Priority must be >= 1 and <= 5",
            )
        update_data = data.model_dump()

        return self.repo.update(db, todo, update_data)

    def update_todo_patch(self, db: Session, todo_id: int, data: TodoUpdate) -> Todo:
        existed = self.repo.get_by_title(db, str(data.title))
        if existed and existed.id != todo_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Title already exists"
            )
        if data.priority < 1 or data.priority > 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Priority must be >= 1 and <= 5",
            )
        todo = self.get_todo(db, todo_id)
        update_data = data.model_dump(exclude_unset=True)

        return self.repo.update(db, todo, update_data)

    def delete_todo(self, db: Session, todo_id: int) -> None:
        todo = self.get_todo(db, todo_id)
        self.repo.delete(db, todo)
