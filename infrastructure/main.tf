terraform {
  required_version = ">= 1.5.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "infrastructure_info" {
  filename = "${path.module}/infrastructure-info.txt"

  content = <<-EOT
    Acme Retail Inventory Management System
    Group: 17
    Capstone Level: Foundation

    Infrastructure as Code is managed using Terraform.

    Current deployment model:
    - FastAPI application
    - In-memory product storage
    - Docker container configuration prepared
    - Cloud deployment not yet provisioned

    This local Terraform resource is used for validating
    the Infrastructure as Code structure without creating
    cloud resources.
  EOT
}