import os
from src.Config import Config
import pandas as pd
from src.logger import get_logger
from sklearn.model_selection import train_test_split


logger = get_logger("Data_Splitter")

def dividing_data_into_train_and_test() -> None:
    """
    This function splits the data into train and test sets for preventing Data Leakage
    :return:
    """

    try:
        # Fetching raw data from data folder
        logger.debug("Starting data splitting")
        data = pd.read_csv(Config.RAW_DATA)
        logger.debug("Raw Data fetched")

        # Splitting data into
        logger.debug("Splitting data into train and test")
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(Config.TRAINING_DATA, index=False)
        test.to_csv(Config.TESTING_DATA, index=False)
        logger.info(f"Data is spilt into train and test and saved to {Config.TRAINING_DATA} & {Config.TESTING_DATA}")

    except Exception as e:
        logger.error(f"Encountered an error: {e}")

if __name__ == "__main__":
    dividing_data_into_train_and_test()

