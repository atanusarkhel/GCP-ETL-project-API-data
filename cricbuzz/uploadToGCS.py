import json
from google.cloud import storage
from google.oauth2 import service_account

def uploadToGCS():
    bucket_name = "cricbuzz"
    destination_blob_name = "matches_list.json"
    source_file_name = "dataset/matches_list.json"
    # Path to your service account JSON key file
    service_account_json_path = "E:/GCP service account/famous-crossing-445714-p4-112578d13bc7.json"

    credentials=service_account.Credentials.from_service_account_file(service_account_json_path)

    storage_client=storage.Client(credentials=credentials)
    bucket=storage_client.bucket(bucket_name)
    blob=bucket.blob(destination_blob_name)

    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to GCS as {destination_blob_name}."
    )

uploadToGCS()