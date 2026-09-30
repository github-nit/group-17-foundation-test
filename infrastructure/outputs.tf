output "project_name" {
  description = "Project name used by the Terraform configuration."
  value       = var.project_name
}

output "environment" {
  description = "Deployment environment used by the Terraform configuration."
  value       = var.environment
}

output "infrastructure_info_file" {
  description = "Path of the locally generated infrastructure information file."
  value       = local_file.infrastructure_info.filename
}