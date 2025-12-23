from fastapi import FastAPI

from configs.env import settings_config
from controllers.todo_controller import todo_router
from core.app_logging import setup_logging
from middlewares.db_session import DBSessionMiddleware
from middlewares.trace_id import TraceIdMiddleware

app = FastAPI()

settings = settings_config()
setup_logging(sql_echo=(settings.environment == "DEV"))

app.include_router(todo_router, prefix="/todos", tags=["Todos"])

app.add_middleware(DBSessionMiddleware)
app.add_middleware(TraceIdMiddleware)
