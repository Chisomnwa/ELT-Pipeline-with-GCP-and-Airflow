# backend bucket that will be used to manage the teraform state file remotely 
resource "google_storage_bucket" "terraform_backend" {
  name          = "medical_data_backend_bucket"
  location      = "US"
  force_destroy = true

  versioning {
    enabled = true
  }

  labels = {
    environment = "dev"
    owner       = "chisom"
  }
}