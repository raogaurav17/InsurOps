import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd
from src.logger import get_logger
load_dotenv()

logger = get_logger("Data Injection to MongoDB")

def load_data_to_mongo() -> None:
    """
    Inject data into MongoDB Atlas
    :return:
    """
    try:
        uri = os.getenv('MONGO_URI')

        logger.info("Connecting to MongoDB Atlas")

        client = MongoClient(uri)
        db = client["InsurOps-data"]
        collection = db["records"]

        logger.info("Connected to MongoDB Atlas")

        logger.debug("Getting data from remote repository 'data'")

        df = pd.read_csv("..\\data\\insurance.csv")

        logger.debug("Successfully loaded data from remote repository 'data'")

        data = df.to_dict('records')
        logger.debug("Converted data to json format")

        logger.debug("Inserting data into MongoDB Atlas")
        collection.insert_many(data)
        logger.debug("Successfully inserted data into MongoDB Atlas")

    except FileNotFoundError:
        logger.error("File not found")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    load_data_to_mongo()




