from textSumarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSumarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSumarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSumarizer.pipeline.stage_04_model_trainer import ModeltrainerPipeline
from textSumarizer.pipeline.stage_05_model_evaluation import ModelevaluationPipeline

from textSumarizer.logging import logger

# STAGE_NAME = "Data Ingestion Pipeline"

# try:
#     logger.info(f"----------{STAGE_NAME} Started !!----------")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f"----------{STAGE_NAME} Ended !!----------")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Data Validation Pipeline"

try:
    logger.info(f"----------{STAGE_NAME} Started !!----------")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"----------{STAGE_NAME} Ended !!----------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Pipeline"

try:
    logger.info(f"----------{STAGE_NAME} Started !!----------")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"----------{STAGE_NAME} Ended !!----------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Pipeline"

try:
    logger.info(f"----------{STAGE_NAME} Started !!----------")
    model_trainer = ModeltrainerPipeline()
    model_trainer.main()
    logger.info(f"----------{STAGE_NAME} Ended !!----------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Pipeline"

try:
    logger.info(f"----------{STAGE_NAME} Started !!----------")
    model_evaluation = ModelevaluationPipeline()
    model_evaluation.main()
    logger.info(f"----------{STAGE_NAME} Ended !!----------")
except Exception as e:
    logger.exception(e)
    raise e