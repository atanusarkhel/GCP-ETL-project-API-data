import json
from google.cloud import storage
from google.oauth2 import service_account


def uploadToGCS(bucket,destination_file,source_file):

    # Path to your service account JSON key file
    service_account_json_path = "E:/GCP service account/famous-crossing-445714-p4-112578d13bc7.json"

    credentials=service_account.Credentials.from_service_account_file(service_account_json_path)

    storage_client=storage.Client(credentials=credentials)
    bucket=storage_client.bucket(bucket)
    blob=bucket.blob(destination_file)
    if not blob.exists():
        generation_match_precondition = 0
        blob.upload_from_filename(source_file, if_generation_match=generation_match_precondition)
        print( f"File {source_file} uploaded to GCS as {destination_file}.")

    else:
        print(f"{destination_file} already present inside GCS")


uploadToGCS("cricbuzz", "matches_list.json","dataset/matches_list.json")