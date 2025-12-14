from datetime import datetime

class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self, now: datetime | None = None) -> bool:
        if now is None:
            now = datetime.now()
        return True if self.due_date < now and self.status == "todo" else False


    def __str__(self) -> str:
        return f"[{self.status.upper()}] {self.description} (Hạn: {self.due_date.strftime("%Y-%m-%d")})"