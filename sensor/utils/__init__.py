import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))

    except Exception as e:
        raise SensorException(e,sys)    

        
