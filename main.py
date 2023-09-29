from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data ingestion stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.run()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
except  Exception as e:
    logger.exception(e)
    raise e