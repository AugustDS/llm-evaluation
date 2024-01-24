from sqlalchemy import Column, String, TIMESTAMP
from app.sql.database import Base


class DbUser(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    signup_date = Column(TIMESTAMP)
    userSubIndustry = Column(String, unique=False, index=True)
    enabled = Column(String, unique=True, index=True)
    organisation_id = Column(String, unique=True, index=True)


class DbStandardQuestionsTemplate(Base):
    __tablename__ = "standard_questions_template"

    question_id = Column(String, primary_key=True, index=True)
    standard_question = Column(String, unique=True, index=True)
    question_topic = Column(String, index=True)
    user_id = Column(String, index=True)
    scope = Column(String, index=True)
    connected_project_data = Column(String, index=True)
    organisation_id = Column(String, index=True)
    project_analysis_id = Column(String, index=True)


class DbStandardQuestionsAnswers(Base):
    __tablename__ = "standard_questions_answers"

    answer_id = Column(String, primary_key=True, index=True)
    project_id = Column(String, unique=True, index=True)
    question_answer = Column(String, index=True)
    question_topic = Column(String, index=True)
    user_id = Column(String, index=True)
    standard_question = Column(String, index=True)
    question_id = Column(String, index=True)
    organisation_id = Column(String, index=True)
    answer_source = Column(String, index=True)


class DbSqEvaluation(Base):
    __tablename__ = "sq_evaluation"

    user_id = Column(String, primary_key=True, index=True)
    standard_question = Column(String, index=True)
    ground_truth = Column(String, index=True)
    project_id = Column(String, unique=True, index=True)
    question_topic = Column(String, index=True)
    scope = Column(String, index=True)
    connected_project_data = Column(String, index=True)
    organisation_id = Column(String, index=True)
    question_id = Column(String, index=True)
