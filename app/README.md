\# AI-Driven Cloud \& DevSecOps Modernization of an Inventory Management System



\## Project Information



\*\*Customer:\*\* Acme Retail Ltd.  

\*\*Group:\*\* 17  

\*\*Capstone Level:\*\* Foundation  

\*\*Repository:\*\* `group17-foundation`



\---



\## 1. Project Overview



This project modernizes an Inventory Management System (IMS) for Acme Retail Ltd. using an AI-driven Cloud \& DevSecOps engineering approach.



The project focuses on creating a secure, maintainable, testable, and deployment-ready application together with infrastructure automation, CI/CD, security validation, documentation, and AI Engineering Specifications.



\---



\## 2. Business Problem



Acme Retail Ltd. currently faces several engineering challenges:



\- Manual infrastructure provisioning

\- Manual application deployments

\- No Infrastructure as Code (IaC)

\- No standardized CI/CD pipeline

\- Weak security validation

\- Poor engineering documentation

\- No standardized AI Engineering Specifications



The goal is to address these challenges through a structured Cloud \& DevSecOps modernization approach.



\---



\## 3. Application



The application is an Inventory Management System built using Python and FastAPI.



The current Foundation implementation provides:



\- Product creation

\- Product listing

\- Product search

\- Product update

\- Product deletion

\- Stock increase

\- Stock decrease

\- Low-stock detection

\- Out-of-stock detection

\- Inventory status

\- Health check

\- Input validation

\- Duplicate SKU protection



\### Inventory Status



Products can have one of three inventory statuses:



\- `In Stock`

\- `Low Stock`

\- `Out of Stock`



\---



\## 4. Technology Stack



\### Application



\- Python

\- FastAPI

\- Uvicorn

\- Pydantic



\### Testing



\- Pytest



\### Containerization



\- Docker

\- Dockerfile

\- `.dockerignore`



\### DevSecOps



The planned engineering toolchain includes:



\- Git

\- GitHub

\- GitHub Actions

\- Terraform

\- Trivy

\- Checkov

\- Gitleaks



\### Documentation



\- Markdown

\- Mermaid

\- Draw.io



\---



\## 5. Current Application Architecture



The current application is implemented as a single deployable FastAPI application.



```text

Client

&#x20;  |

&#x20;  v

FastAPI Application

&#x20;  |

&#x20;  +--> Product Management

&#x20;  |

&#x20;  +--> Inventory Management

&#x20;  |

&#x20;  +--> Search

&#x20;  |

&#x20;  +--> Inventory Status

&#x20;  |

&#x20;  +--> Health Check

