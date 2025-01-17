CREATE OR REPLACE TABLE `{{ params.PROJECT_ID }}.{{ params.TRANSFORMED_DATASET_ID }}.{{ params.COUNTRY }}_table` AS
SELECT *
FROM `{{ params.PROJECT_ID }}.{{ params.STAGING_DATASET_ID }}.global_data`
WHERE country = '{{ params.COUNTRY }}';
