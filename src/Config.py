import os

class Config:

    # Logger Configs
    LOG_DIR: str = os.getenv("LOG_DIR", "logs")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    MAX_BYTES: int = int(os.getenv("LOG_MAX_BYTES", 5 * 1024 * 1024))  # 5 MB
    BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", 3))

    # Data Dir and Files (Used in various Configs)
    DATA_DIR: str = os.getenv("DATA_DIR", "data")
    RAW_DATA: str = os.getenv("RAW_DATA", "data\\raw_data.csv")

    # Mongo DB Atlas Configs
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE", "InsurOps-data")
    MONGO_RECORDS: str = os.getenv("MONGO_RECORDS", "records")
