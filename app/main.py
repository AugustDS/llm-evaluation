from app.core.config import Config
from app.core.logging import CustomLogger
from app.services.dataset import DataSet
from app.services.evaluation import Evaluation

config = Config()
logger = CustomLogger()


def main():
    logger.log('info', "Build Datases.")
    ds = DataSet.build_dataset(
        user_id=config.USER_ID, project_id=config.PROJECT_ID)
    logger.log('info', "Evaluate Datases.")
    results = Evaluation.evaluate(dataset=ds)
    logger.log('info', "Results:")
    logger.log('info', results)


if __name__ == "__main__":
    main()
