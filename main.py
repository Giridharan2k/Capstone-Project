from src.KidneyProject import logger
from src.KidneyProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<<<")
    logger.info(f">>>>Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e