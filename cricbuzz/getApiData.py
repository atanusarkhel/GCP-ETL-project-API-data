import requests
import pandas as pd
import logging
import json
import os

def getApiMetadataFile():
    ApiDataFileMetadataFile="config/cricbuzz_api_config.csv"
    ApiDataFileMetadataDF=pd.read_csv(ApiDataFileMetadataFile)
    return ApiDataFileMetadataDF


def hitAPI(url,key,host):
    api_headers = {
        "x-rapidapi-key": key,
        "x-rapidapi-host": host
    }
    # checks for any exception during running
    try:
        api_dataset = requests.get(url, headers=api_headers)
        if 200 <= api_dataset.status_code < 300:
            logging.info("API HIT successful and returned data")
            return api_dataset.json()


    except Exception as e:
        logging.error(f"Error Occured- {e}")

def saveApiResponseJSON(file_name,data):
    try:
        with open(file_name, "w") as f:
            json.dump(data, f)
            logging.info(f"File Saved as : {file_name}")

    except Exception as e:
        logging.error(f"Error Occurred: {e}")


def getApiData(api_name):

    ApiDataFileMetadataFile = "config/cricbuzz_api_config.csv"
    apimetadata = pd.read_csv(ApiDataFileMetadataFile)

    api_metadata_dataset=apimetadata[apimetadata["api_name"]==api_name]

    api_url=api_metadata_dataset["url"].iloc[0]
    api_key=api_metadata_dataset["x-rapidapi-key"].iloc[0]
    api_host=api_metadata_dataset["x-rapidapi-host"].iloc[0]

    json_file_name = f"dataset/{api_name}.json"

    if not (os.path.exists(json_file_name)):
        json_dataset=hitAPI(api_url,api_key,api_host)
        saveApiResponseJSON(json_file_name,json_dataset)
    else:
        logging.info(f"{json_file_name} already present!!")

def getAllApiData():
    ApiDataFileMetadataFile = "config/cricbuzz_api_config.csv"
    read_all_metadata=pd.read_csv(ApiDataFileMetadataFile)
    read_all_metadata=read_all_metadata[read_all_metadata["api_name"].notna()]
    api_name_list=read_all_metadata["api_name"].tolist()
    for i in api_name_list:
        logging.info(f"calling API {i}")
        getApiData(i)

#getAllApiData()