from configs.database import SessionLocal
from models import Todo

def seed_todos():
    db = SessionLocal()
    try:
        if db.query(Todo).count() == 0:
            db.add_all([
                Todo(title="Làm việc", description="Example1", priority=5, done=False),
                Todo(title="Học tập", description="Example2", priority=4, done=False),
                Todo(title="Thực hành", description="Example3", priority=3, done=True),
                Todo(title="Ăn uống", description="Example2", priority=2, done=True),
                Todo(title="Ngủ nghỉ", description="Example1", priority=1, done=False)
            ])
            db.commit()
    finally:
        db.close()
if __name__ == "__main__":
    seed_todos()