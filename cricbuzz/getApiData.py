import requests as rq
import pandas as pd

def getApiMetadataFile():
    ApiDataFileMetadataFile="config/cricbuzz_api_config.csv"

    ApiDataFileMetadataDF=pd.read_csv(ApiDataFileMetadataFile)
    # print(ApiDataFileMetadataDF)
    return ApiDataFileMetadataDF


def getApiData(api_name):
    apimetadata=getApiMetadataFile()
    api_name="matches_list"
    api_url=apimetadata[apimetadata["url"]==api_name]
    print(api_url)
    #url=apimetadata

getApiData()




