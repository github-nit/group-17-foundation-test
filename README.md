# AI-Driven Cloud & DevSecOps Modernization of an Inventory Management System

## 1. Project Overview

This project modernizes the Inventory Management System (IMS) for Acme Retail Ltd. using Cloud & DevSecOps engineering practices.

The solution focuses mainly on:

- Automated application testing
- Containerization with Docker
- Infrastructure as Code with Terraform
- CI/CD automation using GitHub Actions
- Security validation using Gitleaks, Trivy, and Checkov
- AI Engineering Specifications
- Architecture and engineering documentation
- Reproducible local validation

## 2. Business Context

Acme Retail Ltd. is modernizing its software engineering and delivery practices.

The modernization addresses:

- Manual infrastructure provisioning
- Manual application deployments
- Lack of Infrastructure as Code
- Lack of standardized CI/CD
- Weak security validation
- Poor documentation
- Lack of AI engineering standards

The project provides a production-inspired solution while remaining reproducible locally without requiring dedicated cloud resources.

## 3. Application

The application is a Python FastAPI Inventory Management System.

### Application capabilities

- Create products
- Retrieve products
- Update products
- Delete products
- Search products
- Add stock
- Remove stock
- Identify low-stock products
- Identify out-of-stock products
- Check product inventory status
- Health check endpoint

### Product information

Each product contains:

- SKU
- Product name
- Category
- Price
- Quantity
- Supplier
- Reorder level

### Storage

The current Foundation implementation uses temporary in-memory storage.

No database is required for the current implementation.

The decision to use in-memory storage is documented in:

```text
engineering-decisions/ADR-001-in-memory-storage.md
