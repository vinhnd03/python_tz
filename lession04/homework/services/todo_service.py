from fastapi import HTTPException
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.todo_out_schema import TodoOut

_todos: list[dict] = []
_id_counter = 1


def create_todo(new_todo: TodoCreate) -> TodoOut:
    global _id_counter

    for todo in _todos:
        if todo["title"].casefold() == new_todo.title.casefold():
            raise HTTPException(status_code=409, detail="Todo title already exists")

    stored_todo = {
        "id": _id_counter,
        "title": new_todo.title,
        "description": new_todo.description,
        "priority": new_todo.priority,
        "done": new_todo.done,
    }

    _todos.append(stored_todo)
    _id_counter += 1

    return TodoOut(**stored_todo)


def get_all_todos(
    done: bool | None = None, keyword: str | None = None, limit: int = 10
) -> list[TodoOut]:
    todo_list = _todos
    if done is not None:
        todo_list = [todo for todo in todo_list if todo["done"] == done]
    
    if keyword is not None:
        todo_list = [todo for todo in todo_list if keyword.lower() in todo["title"].lower()]
        
    return [
        TodoOut(**todo)
        for todo in todo_list[:limit]
    ]
    
def get_todo_by_id(id: int) -> TodoOut:
    for todo in _todos:
        if todo["id"] == id:
            return TodoOut(**todo)
    raise HTTPException(404, "Todo not found")

def put_todo (id: int, data: TodoCreate) -> TodoOut:
    for todo in _todos:
        if todo["id"] != id and todo["title"].casefold() == data.title.casefold():
            raise HTTPException(status_code=409, detail="Todo title already exists")
    for todo in _todos:
        if todo["id"] == id:
            todo.update(data.model_dump())
            todo["id"] = id
            return TodoOut(**todo)
    raise HTTPException(404, "Todo not found")

def patch_todo (id: int, data: TodoUpdate) -> TodoOut:
    if data.title is not None:
        for todo in _todos:
            if todo["id"] != id and todo["title"].casefold() == data.title.casefold():
                raise HTTPException(status_code=409, detail="Todo title already exists")
    for todo in _todos:
        if todo["id"] == id:
            updates = data.model_dump(exclude_unset=True)
            todo.update(updates)
            return TodoOut(**todo)
    raise HTTPException(404, "Todo not found") 
    
def delete_todo (id: int) -> None:
    for index, todo in enumerate(_todos):
        if todo["id"] == id:
            _todos.pop(index)
            return
    raise HTTPException(404, "Todo not found") 
        