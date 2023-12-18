from textSumarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSumarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSumarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSumarizer.logging import logger

STAGE_NAME = "Data Ingestion Pipeline"

try:
    logger.info(f"----------{STAGE_NAME} Started !!----------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----------{STAGE_NAME} Ended !!----------")
except Exception as e:
    logger.exception(e)
    raise e

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

