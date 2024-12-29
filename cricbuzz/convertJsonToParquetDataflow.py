import apache_beam as beam
from apache_beam.transforms.combiners import Top
from apache_beam.options.pipeline_options import PipelineOptions
import json
from apache_beam.io import ReadFromText
import pyarrow as pa
import pyarrow.parquet as pq
import argparse
import logging


# convert json data to dictionary
def jsonToDict(json_string):
    try:
        dict_data=json.loads(json_string)
        return dict_data
    except Exception as e:
        print(f"Error - {e}")
        return None


# get pyarrow table schema dynamically from json data(dictionary)
def inferSchemaFromJson(json_data):
    try:
        schema=pa.schema([(key, pa.string()) for key in json_data.keys()])
        return schema
    except Exception as e:
        print(f"Error - {e}")
        return None


# convert json_data(dictionary) to pyarrow table for writing into parquet
def convertToArrowTable(json_data,schema):
    try:
        pa_table_Data=pa.table([json_data],schema=schema)
        return pa_table_Data

    except Exception as e:
        print(f"Error - {e}")
        return None


# writing json data into parquet
def writeToParquet(json_data,schema,output_file):
    try:
        pa_table=pa.table(json_data,schema=schema)
        pq.write_table(pa_table, output_file, compression='snappy')
    except Exception as e:
        print(f"Error writing to parquet- {e}")
        return None

options= PipelineOptions(
    flags=None,
    runner='DirectRunner',
    project="famous-crossing-445714-p4",
    region="us-east1",
    temp_location="gs://cricbuzz/temp/",
    staging_location="gs://cricbuzz/staging_loc/",
    output_location="gs://cricbuzz/transform_parquet/",
    job_name='json-to-parquet',
    save_main_session=True
)

def run(input_folder,output_folder):
    with beam.Pipeline(options=options) as p:
        input_files=(
            p
            | 'read Files' >> ReadFromText(input_folder)
            | 'parse json' >> beam.Map(jsonToDict)
            | 'Infer Schema' >> beam.Map(lambda x: inferSchemaFromJson(x) if x else None)
        )

        schema=(
            input_files
            | 'extract schema' >> beam.Filter(lambda x : x if x else None)
            | 'First Schema'  >> Top.Of(1, key=lambda x: 1)
            | 'Get Schema'   >> beam.Map(lambda x: x[0])
        )
        input_files | 'Convert to Arrow table' >> beam.Map(lambda x: convertToArrowTable(x,schema) if x else None) \
                    | 'Write to Parquet' >> beam.Map(lambda x : writeToParquet([x],schema, output_folder))

if __name__=='__main__':
    input_folder='gs://cricbuzz/raw_json/'
    output_folder='gs://cricbuzz/output-folder/'

    run(input_folder,output_folder)