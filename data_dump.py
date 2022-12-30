import pymongo
import pandas as pd
import json
from sensor.config import mongo_client

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://ineuron:12345@cluster0.afy4g.mongodb.net/test")


DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns are:{df.shape}")

# In mongodb we require data in json format so we convert dataframe to json format 
df.reset_index(drop=True,inplace=True)
json_record= list(json.loads(df.T.to_json()).values())
print(json_record[0])

# we get json format data then insert data into mongodb
mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


