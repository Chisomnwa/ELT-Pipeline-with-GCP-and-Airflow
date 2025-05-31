# ELT Data Pipeline with GCP and Airflow

This project demonstrates how to build an **ELT (Extract, Load, Transform)** data pipeline to process **1 million records** using **Google Cloud Platform (GCP)** and **Apache Airflow**. The pipeline extracts data from Google Cloud Storage (GCS), loads it into BigQuery, and transforms it to create country-specific tables and views for analysis.

---

## Project Requirements
The medical research team of a certain organization receives this global health statistics file containing disease data for all countries.

Each country’s Health Minister should have access only to their respective country’s medical data. Additionally, they need the ability to analyze diseases for which no treatment or vaccination is currently available.

## Challenges
The data is currently provided as a single file containing over 1 million records for all countries.
due to the confidential nature of the data, sharing the entire file with everyone is not feasible.
analyzing such a CSV file to extract meaningful insights is complex and inefficient.
Objective
Develop a robust data analytics solution to securely manage and filter this data securely, ensuring restricted and enabling efficient analysis of diseases without available treatment or vaccination.

## Features

- Provision resources(data architecture) with Terraform.
- Upload data to Google Cloud Storage.
- Extract data from GCS in CSV format.
- Load raw data into a staging table in BigQuery.
- Transform data into country-specific tables and reporting views.
- Use Apache Airflow to orchestrate the pipeline.
- Generate clean and structured datasets for analysis.

---

## Architecture

![image](https://github.com/Chisomnwa/ELT-Pipeline-with-GCP-and-Airflow/blob/main/project_files/data_pipeline_architecture.png)


### Workflow
1. **Extract**: Check for file existence in GCS.
2. **Load**: Load raw CSV data into a BigQuery staging table.
3. **Transform**:
   - Create country-specific tables in the transform layer.
   - Generate reporting views for each country with filtered insights.

### Data Layers
1. **Staging Layer**: Raw data from the CSV file.
2. **Transform Layer**: Cleaned and transformed tables.
3. **Reporting Layer**: Views optimized for analysis and reporting.

---

## Requirements

### Tools and Services
- **Terraform**:
  - For provisioning of data infrastructure
- **Google Cloud Platform (GCP)**:
  - Google Compute Engine (for Airflow)
  - BigQuery
  - Cloud Storage
- **Apache Airflow**:
  - Airflow with Google Cloud providers


---

## Setup Instructions

### Prerequisites
1. Terraform Installed.
  - Use this [blog](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for Terraform Installation on your local machine.
3. A Google Cloud project with:
   - BigQuery, Cloud Storage and Compute Engine API enabled.
   - Service account with required permissions.
4. Apache Airflow installed.
   - Use this [blog](https://www.techtrapture.com/blogs/673a2625dd155b000b7cdb3b) for Airflow Installation on your Google Cloud Compute Engine instance(Virtual Machine). 

## End Result

### Airflow Pipeline

![image](https://github.com/Chisomnwa/ELT-Pipeline-with-GCP-and-Airflow/blob/main/project_files/airflow_pipeline.png)


### Looker Studio Report

![image](https://github.com/Chisomnwa/ELT-Pipeline-with-GCP-and-Airflow/blob/main/project_files/google_looker_studio_dashboard.png)

---
 ## Extra Resources
 - [Medium Article](https://medium.com/towards-data-engineering/elt-data-pipeline-with-gcp-and-apache-airflow-86c6d72544ef)
   