# Configuring the backend bucket
terraform {
  backend "gcs" {
    bucket = "medical_data_backend_bucket"
    prefix = "terraform/state"
  }
}
