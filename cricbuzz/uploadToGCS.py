import json
import logging
import os
from google.cloud import storage
from google.oauth2 import service_account


def uploadToGCS(bucket,destination_file,source_file):

    destination_file="raw_json/"+destination_file

    # Path to your service account JSON key file
    service_account_json_path = "E:/GCP service account/famous-crossing-445714-p4-112578d13bc7.json"

    try:
        credentials=service_account.Credentials.from_service_account_file(service_account_json_path)

        storage_client=storage.Client(credentials=credentials)
        bucket=storage_client.bucket(bucket)
        blob=bucket.blob(destination_file)

        if not blob.exists():
            generation_match_precondition = 0
            blob.upload_from_filename(source_file, if_generation_match=generation_match_precondition)
            logging.info( f"File {source_file} uploaded to GCS as {destination_file}.")

        else:
            logging.info(f"{destination_file} already present inside GCS!!!")

    except Exception as e:
        logging.error(f"Error Occurred- {e}")

def uploadAllFileToGCS():
    source_file_location="dataset/"
    all_file_names=[f for f in os.listdir(source_file_location) if os.path.isfile(os.path.join(source_file_location,f))]
    source_file_names=[os.path.join(source_file_location,f) for f in all_file_names]
    logging.info(f"source files are - {source_file_names}")
    logging.info(f"dest files are - {all_file_names}")

    for i in range(len(all_file_names)):
        logging.info(f"uploading file- {all_file_names[i]}")
        uploadToGCS("cricbuzz",all_file_names[i],source_file_names[i])


#uploadToGCS("cricbuzz", "matches_list.json","dataset/matches_list.json")
#uploadAllFileToGCS()