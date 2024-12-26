import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

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