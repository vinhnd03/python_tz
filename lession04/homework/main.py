from fastapi import FastAPI
from controllers.todo_controller import todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/todos", tags=["Todos"])