from textSumarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSumarizer.pipeline.stage_02_data_ingestion import DataValidationPipeline
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
