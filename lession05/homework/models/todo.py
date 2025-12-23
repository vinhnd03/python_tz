from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.mixins import TimeMixin


class Todo(TimeMixin, Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    priority: Mapped[int] = mapped_column(nullable=False)
    done: Mapped[bool] = mapped_column(nullable=False, default=False)

