"""
Purpose: This DAG script demonstrates how to load data from GCS to BigQuery
         and create country-specific tables and views for reporting.

Note: This script contains placeholder values that you need to replace with your actual values
to make it functional in your environment.

1. Replace the following placeholders:
    - `project_id`: Your Google Cloud Project ID
    - `dataset_id`: The name of the staging dataset where the raw data will be loaded.
    - `transformed_dataset_id`: The dataset name where the transformed data will be stored.
    - `reporting_dataset`: The name of the final reporting views.
    - `bucket`: The name of the GSC bucket where your CSV file is be stored.
    - `object`: The path to the CSV file in the GCS bucket.
    - 'countries': The list of countries' names (modify as per your requirements).

2. Ensure the following:
    - The service account used for Airflow has permissions for GCS or BigQuery operations.
    - The datasets (`staging_dataset`, `transformed_dataset`, and `reporting dataset` exist in BigQuery).

3. Adjust the DAG schedule and other parameters as needed for your use case.

4. Create a virtual environment
Happy coding! 
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.operators.bigquery import \
    BigQueryInsertJobOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import \
    GCSToBigQueryOperator
from airflow.models import Variable

# DAG default arguments
default_args = {
    'owner':'chisom',
    'retries':1,
}

# Define project, datasets and table details
project_id = 'elt-pipeline-gcp-and-airflow' # Change the project id
staging_dataset_id = 'staging_dataset'
transformed_dataset_id = 'transformed_dataset'
reporting_dataset_id = 'reporting_dataset'
source_table = f'{project_id}.{staging_dataset_id}.global_data' # the main table to hold the raw data
countries = ['Nigeria', 'USA', 'Germany', 'India', 'Japan', 'France', 'Canada', 'Italy']
QUERY_SQL_PATH = "../sql_scripts/"


# DAG Definition
with DAG (
    dag_id='elt_pipeline',
    default_args=default_args,
    description='Load a CSV file from GCS to BigQuery and create country-specific tables',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bigquery', 'gcs', 'csv'],
) as dag:
    
    # Task 1: Check if CSV file exists in the GCS
    check_if_file_exists = GCSObjectExistenceSensor(
        task_id = 'check_if_file_exists',
        bucket='medical_global_data', # Replace with your bucket name
        object='global_health_data.csv', # Replace with the file path in the bucket
        timeout=300, # Maximum wait time in seconds
        poke_interval=30, # The interval in seconds to check again
        mode='poke',
    )

    # Task 2: Load CSV file from GCS to BigQuery
    load_csv_to_bigquery = GCSToBigQueryOperator(
        task_id='load_csv_to_bigquery',
        bucket='medical_global_data', # Replace with your bucket name
        source_objects=['global_health_data.csv'], # Path to your file in thebucket
        destination_project_dataset_table=source_table,
        source_format='CSV',
        allow_jagged_rows=True,
        ignore_unknown_values=True,
        write_disposition='WRITE_TRUNCATE', # Options: WRITE TRUNCATE, WRITE APPEND, WRITE EMPTY
        skip_leading_rows=1, # Skip header row
        field_delimiter=',',
        autodetect=True,
    )

    # Task 3: Create country-specific table and store them in a list
    create_table_tasks = [] # List to store table creation tasks
    create_view_tasks = [] # List to store view creation tasks
    # Iterate over countries
    for country in countries:
        # Task to create country-specific tables
        create_table_task = BigQueryInsertJobOperator(
            task_id=f'create_table_{country.lower()}',
            configuration={
                "query": {
                    "query": "{% include '" + QUERY_SQL_PATH + "create_table.sql' %}",
                    "useLegacySql": False,
                }
            },
            params={
                "PROJECT_ID": Variable.get("project_id"),
                "STAGING_DATASET_ID": Variable.get("staging_dataset_id"),
                "TRANSFORMED_DATASET_ID": Variable.get("transformed_dataset_id"),
                "COUNTRY": country.lower(),
            },
            location='US',  # Specify the location for BigQuery jobs
        )

        # Task to create country-specific views
        create_view_task = BigQueryInsertJobOperator(
            task_id=f'create_view_{country.lower()}',
            configuration={
                "query": {
                    "query": "{% include '" + QUERY_SQL_PATH + "create_view.sql' %}",
                    "useLegacySql": False,
                }
            },
            params={
                "PROJECT_ID": Variable.get("project_id"),
                "TRANSFORMED_DATASET_ID": Variable.get("transformed_dataset_id"),
                "REPORTING_DATASET_ID": Variable.get("reporting_dataset_id"),
                "COUNTRY": country.lower(),
            },
            location='US',
        )

        # Set dependencies
        create_table_task.set_upstream(load_csv_to_bigquery)
        create_view_task.set_upstream(create_table_task)

        create_table_tasks.append(create_table_task) # Add table creation task to list
        create_view_tasks.append(create_view_task) # Add view creation task to list

    # Dummy success task to run after all the tables and views are created
    success_task= EmptyOperator(
        task_id='success_task'
    )
      
    # Define task dependencies
    check_if_file_exists >> load_csv_to_bigquery
    for create_table_task, create_view_task in zip(create_table_tasks, create_view_tasks):
        create_table_task >> create_view_task >> success_task
