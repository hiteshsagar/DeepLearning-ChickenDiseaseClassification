from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = 'Data ingestion stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.run()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
except  Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.run()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
except  Exception as e:
    logger.exception(e)
    raise e