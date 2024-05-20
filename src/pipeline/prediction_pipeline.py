import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logging import logging
from src.utils.utils import load_object


class PredictPipeline:
    def __new__(self):
        print("new project")

    def __init__(self):
        print("mlops project")

    def predict(self):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            #features are from the flask app
            scaled_feature = preprocessor.transform(features)
            pred = model.predict(scaled_feature)

            return pred

        except Exception as e:
            raise customexception(e,sys)
        
class CustomData:
    def __init__(self):
        pass
    def get_as_dataframe(self):
        pass
    
obj=PredictPipeline()