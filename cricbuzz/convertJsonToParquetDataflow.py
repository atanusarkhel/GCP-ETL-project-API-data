import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json
from apache_beam.io import WriteToParquet, ReadFromJson
import pyarrow as pa
import pyarrow.parquet as pq
import argparse
import logging

def jsonToDict(json_data):
    try:
        schema=pa.schema([(key, pa.string()) for key in json_data.keys()])
        return schema
    except Exception as e:
        print(f"Error - {e}")
        return None

def jsonToDict(json_string):
    try:
        dict_data=json.loads(json_string)
        return dict_data
    except Exception as e:
        print(f"Error - {e}")
        return None

def convertToArrowTable(json_data,schema):
    try:
        pa_table_Data=pa.table([json_data],schema=schema)
        return pa_table_Data

    except Exception as e:
        print(f"Error - {e}")
        return None



options= PipelineOptions(
    flags=None,
    runner='DataflowRunner',
    project="famous-crossing-445714-p4",
    region="us-east1",
    temp_location="gs://cricbuzz/temp",
    staging_location="gs://cricbuzz/staging_loc",
    output_location="gs://cricbuzz/transform_parquet",
    job_name="json_to_parquet"
)

def run():
    with beam.Pipeline(options=options) as p:
        pass