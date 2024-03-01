from src.KidneyProject import logger
from src.KidneyProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.KidneyProject.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.KidneyProject.pipeline.stage_03_model_training import Modeltraining
from src.KidneyProject.pipeline.stage_04_model_evaluation_with_mlflow import ModelEvaluating

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

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = Modeltraining()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluating"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = ModelEvaluating()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e