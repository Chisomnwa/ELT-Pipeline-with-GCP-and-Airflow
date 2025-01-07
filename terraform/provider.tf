provider "google" {
  credentials = file("/Users/chisom/elt-pipeline-gcp-and-airflow-5175d5d5325d.json")
  project     = "elt-pipeline-gcp-and-airflow"
  region      = "us-central1"
}
