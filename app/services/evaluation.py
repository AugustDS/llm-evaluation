import ragas
import os
from app.core.config import Config
from datasets import Dataset
from ragas import evaluate
from core.logging import CustomLogger
config = Config()
logger = CustomLogger()
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY

class Evaluation:
    @staticmethod
    def evaluate(dataset: Dataset) -> dict:
        try:
            results = evaluate(dataset)
            logger.info(results)
        except Exception as e:
            logger.error(e)
        return results
 
