from textSumarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
