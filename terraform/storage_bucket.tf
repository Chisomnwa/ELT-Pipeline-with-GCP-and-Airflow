# the nmain bucket that will hold the CSV file containing 1 million records

resource "google_storage_bucket" "medical_global_bucket" {
  name                     = "medical_global_data"
  location                 = "US"
  force_destroy            = true
  public_access_prevention = "enforced"
  labels = {
    environment = "dev"
    project     = "etl-pipeline"
    owner       = "chisom"
  }

  versioning {
    enabled = true
  }
}
