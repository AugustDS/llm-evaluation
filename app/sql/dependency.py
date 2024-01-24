from app.sql.database import SessionLocal
# Later for FastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
