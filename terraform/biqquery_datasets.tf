# Creating the datasets for the 3 different layers that we need for data processing

variable "datasets" {
  default = [
    {
      id            = "staging_dataset"
      friendly_name = "Staging Dataset"
      description   = "Dataset for staging raw data"
      location      = "US"
    },
    {
      id            = "transformed_dataset"
      friendly_name = "Transformed Dataset"
      description   = "Dataset for storing transformed data"
      location      = "US"
    },
    {
      id            = "reporting_dataset"
      friendly_name = "Reporting Dataset"
      description   = "Dataset for final reporting views"
      location      = "US"
    }
  ]
}

resource "google_bigquery_dataset" "datasets" {
  for_each = { for dataset in var.datasets : dataset.id => dataset }

  dataset_id    = each.value.id
  friendly_name = each.value.friendly_name
  description   = each.value.description
  location      = each.value.location

  labels = {
    environment = "dev"
  }

}
