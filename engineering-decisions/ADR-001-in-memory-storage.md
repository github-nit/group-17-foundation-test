\# ADR-001: Use In-Memory Storage for the Foundation Implementation



\## Context



The Acme Retail Inventory Management System requires product and inventory management functionality as part of the Foundation Capstone project.



The current application provides:



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



The Capstone focuses on demonstrating an AI-driven Cloud \& DevSecOps modernization approach, including application engineering, testing, security, CI/CD, infrastructure, and documentation.



\## Problem



A persistent database could be introduced for storing inventory data. However, a database is not required to demonstrate the core Foundation application and DevSecOps workflow.



Adding a database at this stage would introduce additional infrastructure, configuration, dependencies, and local environment requirements.



\## Decision



For the Foundation implementation, the application will use temporary in-memory storage for product data.



The FastAPI application maintains products in application memory while the application is running.



A database will not be included in the current Foundation implementation.



\## Alternatives Considered



\### Alternative 1: PostgreSQL



Use PostgreSQL as a persistent database for inventory data.



\*\*Advantages:\*\*



\- Persistent data storage

\- More production-like data architecture

\- Supports future scaling



\*\*Disadvantages:\*\*



\- Adds database infrastructure

\- Requires additional configuration

\- Increases local development complexity

\- Requires additional application dependencies

\- Not necessary for demonstrating the current Foundation requirements



\### Alternative 2: In-Memory Storage



Store product data directly in application memory.



\*\*Advantages:\*\*



\- Simple implementation

\- Minimal dependencies

\- Easy local testing

\- Easy application startup

\- Supports the current Foundation functionality



\*\*Disadvantages:\*\*



\- Data is lost when the application stops

\- Not suitable for production persistence

\- Does not demonstrate database operations



\## Trade-offs



The project accepts temporary data storage and data loss on application restart in exchange for simplicity and reduced infrastructure complexity.



The decision keeps the Foundation implementation focused on the required application and DevSecOps engineering practices.



\## Consequences



\### Positive Consequences



\- The application remains simple and easy to understand.

\- Local testing does not require a database.

\- The number of application dependencies remains small.

\- The project can be validated without additional database infrastructure.

\- Development can continue even when Docker or database tooling is unavailable.



\### Negative Consequences



\- Inventory data is not persistent.

\- Restarting the application clears the current product data.

\- The implementation is not suitable for production data persistence.



\## Rationale



The Foundation implementation prioritizes demonstrating the Capstone engineering workflow and core inventory functionality without introducing unnecessary infrastructure complexity.



A persistent database can be considered in a future enhancement if the project requirements or deployment design require persistent storage.



\## Status



Accepted

