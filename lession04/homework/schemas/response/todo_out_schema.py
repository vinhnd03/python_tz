from pydantic import BaseModel

class TodoOut(BaseModel):
    id: int
    title: str
    description : str | None
    priority: int
    done: bool