import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import Config

config = Config()

def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    pool = sqlalchemy.create_engine(
        config.RETOOL_POSTGRES_URL
    )
    return pool


engine = connect_with_connector()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
