from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_injestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"      # define the stage name

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

# this we have copied from Pipeline



