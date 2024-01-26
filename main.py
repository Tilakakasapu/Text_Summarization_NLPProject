from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestion
from textSummarizer.pipeline.data_validation_pipeline  import DatavalidationTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
STAGE_NAME = "Data Ingestion stage"
try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e

STAGE_NAME = "Data Valiadation stage"
try:
    
    datavalidation = DatavalidationTrainingPipeline()
    datavalidation.main()

except Exception as e:
    raise e