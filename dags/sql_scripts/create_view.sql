CREATE OR REPLACE VIEW `{{ params.PROJECT_ID }}.{{ params.REPORTING_DATASET_ID }}.{{ params.COUNTRY }}_view` AS
SELECT
    `Year` AS `Year`,
    `Disease Name` AS `disease_name`,
    `Disease Category` AS `disease_category`,
    `Prevalence Rate` AS `prevalence_rate`,
    `Incidence Rate` AS `incidence_rate`
FROM `{{ params.PROJECT_ID }}.{{ params.TRANSFORMED_DATASET_ID }}.{{ params.COUNTRY }}_table`
WHERE `Availability of Vaccines Treatment` = False;
