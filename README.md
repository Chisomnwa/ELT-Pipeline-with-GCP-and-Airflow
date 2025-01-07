# ELT Data Pipeline with GCP and Airflow

This project demonstrates how to build an **ELT (Extract, Load, Transform)** data pipeline to process **1 million records** using **Google Cloud Platform (GCP)** and **Apache Airflow**. The pipeline extracts data from Google Cloud Storage (GCS), loads it into BigQuery, and transforms it to create country-specific tables and views for analysis.

---

## Features

- Provision resources(data architecture)  with Terraform.
- Upload data to Google Cloud Storage.
- Extract data from GCS in CSV format.
- Load raw data into a staging table in BigQuery.
- Transform data into country-specific tables and reporting views.
- Use Apache Airflow to orchestrate the pipeline.
- Generate clean and structured datasets for analysis.

---

## Architecture

![image](https://github.com/user-attachments/assets/87cdc79c-c9a1-4c4d-887a-ab6007394bc7)


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
  - For provisioning of data architecture
- **Google Cloud Platform (GCP)**:
  - Google Compute Engine ( for Airflow )
  - BigQuery
  - Cloud Storage
- **Apache Airflow**:
  - Airflow with Google Cloud providers


---

## Setup Instructions

### Prerequisites
1. Terraform Installed.
2. Use this [blog](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for Terraform Installation on you local machine.
3. A Google Cloud project with:
   - BigQuery and Cloud Storage enabled.
   - Service account with required permissions.
4. Apache Airflow installed.
5. Use [blog](https://www.techtrapture.com/blogs/673a2625dd155b000b7cdb3b) for Airflow Installation on your Google Compyte Engne (Virtual Machine). 

## End Result

### Airflow Pipeline

![image](https://github.com/user-attachments/assets/8e8b8373-9d2a-417b-9fd9-5f42171c06f8)


### Looker Studio Report

![image](https://github.com/user-attachments/assets/d06f0d3e-a1d0-404a-9eb7-c61c85df8257)