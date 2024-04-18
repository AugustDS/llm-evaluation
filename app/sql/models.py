from sqlalchemy import Column, String, Integer
from app.sql.database import Base
from sqlalchemy.dialects.postgresql import JSONB


class DbSampleQATable(Base):
    __tablename__ = "sample_table"

    user_id = Column(Integer, index=True)
    question_answer = Column(String, index=True)
    question_id = Column(Integer, index=True)
    standard_question = Column(String, index=True)
    contexts = Column(JSONB, index=True)
    project_id = Column(Integer, index=True)


class DbSampleEvalTable(Base):
    __tablename__ = "sample_eval"
    user_id = Column(Integer, index=True)
    ground_truths = Column(JSONB, index=True)
    question_id = Column(Integer, index=True)
