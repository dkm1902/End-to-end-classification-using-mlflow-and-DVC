#from src.cnnClassifier import logger 
from cnnClassifier import logger # do have to specify folder??? 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# logger.info("Welcome to cnnClassifier")

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e 