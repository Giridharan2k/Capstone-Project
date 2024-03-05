from src.KidneyProject.config.configuration import ConfigurationManager
from src.KidneyProject.components.model_evaluation_with_mlflow import Evaluation
from src.KidneyProject import logger


STAGE_NAME = "Model Evaluating" 

class ModelEvaluating:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        # evaluation.log_in_to_mlflow() #comment while running the dvc pipeline for faster execution
        
if __name__ == "__main__":
    try:
        logger.info(f"*" * 10)
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj = ModelEvaluating()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e
        