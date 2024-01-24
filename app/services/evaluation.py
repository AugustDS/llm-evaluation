import ragas
import os
from app.core.config import Config
from datasets import Dataset
from ragas import evaluate
from app.core.logging import CustomLogger

config = Config()
logger = CustomLogger()
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY


class Evaluation:
    @staticmethod
    def evaluate(dataset: Dataset) -> dict:
        try:
            results = evaluate(dataset)
            return results
        except Exception as e:
            logger.log('error', e)
        return {}
