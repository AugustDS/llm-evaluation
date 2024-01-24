from app.sql.database import SessionLocal
from app.sql.database import Base
from app.core.config import Config
from app.core.logging import CustomLogger
from app.models.dataframe import DataFrameModel
import pandas as pd

config = Config()
logger = CustomLogger()

class SqlOperations:
    @staticmethod
    def get_dataframe(db: Base) -> DataFrameModel:
        session = SessionLocal()
        try:
            items = session.query(db)
            return pd.read_sql(items.statement, session.bind)
        except Exception as e:
            logger.log('error', e)
            session.rollback()
        finally:
            session.close()
