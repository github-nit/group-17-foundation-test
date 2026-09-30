variable "project_name" {
  description = "Name of the Acme Retail inventory management project."
  type        = string
  default     = "acme-retail-inventory"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "foundation"
}