# Acme Retail Inventory Management System
## Architecture Documentation

**Project:** Foundation AI-Driven Cloud & DevSecOps Capstone Project  
**Customer:** Acme Retail Ltd.  
**Group:** 17  
**Level:** Foundation  
**Application:** Inventory Management System (IMS)

---

## 1. Architecture Overview

The Acme Retail Inventory Management System is a single deployable FastAPI application designed to demonstrate Cloud & DevSecOps engineering practices.

The Foundation solution focuses on:

- Application development using Python and FastAPI
- Automated application testing using Pytest
- Source control using Git and GitHub
- CI/CD automation using GitHub Actions
- Secret scanning using Gitleaks
- Vulnerability scanning using Trivy
- Infrastructure-as-Code validation using Terraform and Checkov
- Containerization using Docker
- Reproducible local validation
- AI Engineering Specifications and engineering documentation

The solution is intentionally kept simple so that the primary focus remains on Cloud & DevSecOps practices.

---

## 2. Business Context

Acme Retail Ltd. requires an Inventory Management System that can be developed and delivered using standardized engineering practices.

The modernization addresses the following engineering problems:

- Manual infrastructure provisioning
- Manual application deployment
- Lack of Infrastructure as Code
- Lack of standardized CI/CD
- Weak automated security validation
- Poor documentation
- Lack of AI engineering standards

The proposed architecture introduces automation and security checks throughout the software delivery lifecycle.

---

## 3. Architecture Goals

The architecture has the following goals:

1. Provide a functional Inventory Management System.
2. Keep the application simple and maintainable.
3. Enable automated testing.
4. Package the application using Docker.
5. Validate infrastructure configuration using Terraform.
6. Integrate security scanning into CI/CD.
7. Provide reproducible local validation.
8. Maintain clear engineering documentation.
9. Support AI-assisted engineering through defined specifications.
10. Provide a foundation that can be extended toward cloud deployment in a future iteration.

---

## 4. Overall Solution Architecture

The current Foundation architecture follows this flow:

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +--------------------+
    |                    |
    v                    v
Python Tests        Security Scans
                    |
                    +--> Gitleaks
                    +--> Trivy
                    +--> Checkov
    |
    v
Docker Build
    |
    v
FastAPI Application
    |
    v
In-Memory Product Storage