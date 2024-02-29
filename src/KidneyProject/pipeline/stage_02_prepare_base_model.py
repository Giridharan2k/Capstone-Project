from src.KidneyProject.config.configuration import ConfigurationManager
from src.KidneyProject.components.prepare_base_model import PrepareBaseModel
from src.KidneyProject import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def _init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f"*" * 10)
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e