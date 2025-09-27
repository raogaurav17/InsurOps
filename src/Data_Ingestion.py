import os
from src.Config import Config
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
from src.logger import get_logger

load_dotenv()
logger = get_logger("Data_Ingestion")

def ingest_data():
    """
    Function to fetch data from remote Mongo DB Atlas Server
    :return:
    """
    try:

        # Connecting to Mongo DB Atlas
        logger.debug("Connecting to MongoDB Atlas")
        uri = os.getenv('MONGO_URI')
        client =  MongoClient(uri)
        db = client[Config.MONGO_DATABASE]
        collections = db[Config.MONGO_RECORDS]

        # Retrieving data from Mongo DB ATLAS
        logger.debug("Trying to fetch data from MongoDB Atlas")
        data = list(collections.find({}))
        logger.info(f"Fetched {len(data)} records from MongoDB Atlas")

        # Saving Records to a csv file using Pandas
        logger.debug("Converting Records to DataFrame")
        df = pd.DataFrame(data)
        logger.info(f"Converted {len(df)} records from MongoDB Atlas")
        logger.debug("Saving data as csv file")
        df.drop(columns=['_id'], inplace=True)  # Dropping MongoDB _id attribute from dataframe
        df.to_csv(Config.RAW_DATA, index=False)
        logger.info(f"Saved {len(df)} records from MongoDB Atlas")


        logger.debug("Data Ingestion Completed")

    except Exception as e:
        logger.error("Error occurred", e)

if __name__ == "__main__":
    ingest_data()