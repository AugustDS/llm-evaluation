from app.core.config import Config
from datasets import Dataset
from app.sql.operations import SqlOperations
from app.sql.models import DbSqEvaluation, DbStandardQuestionsAnswers
from app.models.dataframe import DataFrameModel
from core.logging import CustomLogger
import pandas as pd

config = Config()
logger = CustomLogger()


class DataSet:
    @staticmethod
    def build_dataset(user_id: str, project_id: str = "") -> Dataset:
        logger.info(f'Build evaluation dataset for user_id {user_id}')
        df_ground_truth: DataFrameModel = SqlOperations.get_dataframe(
            DbSqEvaluation)
        df_question_answers: DataFrameModel = SqlOperations.get_dataframe(
            DbStandardQuestionsAnswers)
        df_ground_truth = df_ground_truth[df_ground_truth["user_id"] == user_id]
        df_question_answers = df_question_answers[df_question_answers["user_id"] == user_id]
        if project_id != "":
            logger.info(f'Filter evaluation dataset by project_id {user_id}')
            df_question_answers = df_question_answers[df_question_answers["project_id"] == project_id]

        df = pd.merge(df_ground_truth, df_question_answers,
                      on='question_id', how='inner')
        df = df[["standard_question", "question_answer",
                 "contexts", "ground_truths"]]
        df = df.rename(coulmns={"standard_question": "question",
                       "standard_answer": "answer"})
        logger.info(f'Number of questions to be evaluated {len(df)}.')
        return Dataset.from_pandas(df)
