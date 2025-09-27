from src.Data_Ingestion import ingest_data
from src.logger import get_logger

logger = get_logger("Pipeline")
def main():
    try:
        logger.debug("Starting Pipeline")
        logger.debug("Ingesting Data")
        ingest_data()
        logger.info("Data Ingested")

    except Exception as e:
        logger.error(f"Error occurred {e}")

if __name__ == "__main__":
    main()