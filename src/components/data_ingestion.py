import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexecption
from dataclasses import dataclass
from pathlib import Path
import sys
import os

@dataclass
class DataIngestionConfig:
    pass

class DataIngestion:
    def __init__(self):
        pass

    def initiate_date_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexecption(e,sys)