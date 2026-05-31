# AI-Powered Fake News Detection System

## Project Description

The AI-Powered Fake News Detection System is a web-based platform designed to help users identify potentially misleading or false information in online articles and social media posts. The system analyzes submitted text using natural language processing and machine learning techniques to determine whether the content is likely to be credible or misleading.

The goal of this system is to support media literacy and reduce the spread of misinformation by providing users with automated credibility assessments.

## Documentation

### System Design
- [Specification](SPECIFICATION.md)
- [Architecture](ARCHITECTURE.md)

### Requirements Engineering
- [Stakeholders](STAKEHOLDERS.md)
- [System Requirements (SRD)](REQUIREMENTS.md)

### System Modeling
- [Use Cases](USECASES.md)
- [Test Cases](TESTCASES.md)

### Kanban & GitHub Projects
- [Template Analysis](template_analysis.md)
- [Kanban Explanation](kanban_explanation.md)

### Agile Development
- [Agile Planning](AGILE.md)

### GitHub Agile Tools
- [Issues](../../issues)
- [Project Board](../../projects)
- [Milestones](../../milestones)

### Diagrams
- [State Diagrams](STATE_TRANSITION_DIAGRAMS.md)
- [Activity Diagrams](ACTIVITY_DIAGRAMS.md)

### Domain Modeling and Class Diagram
- [Domain Model](DOMAIN_MODEL.md)
- [Class Diagram](CLASS_DIAGRAM.md)
  
### Reflections
- [Reflection 1](REFLECTION.md)
- [Reflection 2](REFLECTION2.md)
- [Reflection 3](REFLECTION3.md)
- [Reflection 4](reflection.md)
- [Reflection 5](assignment8_reflection.md)
- [Reflection 6](ASSIGNMENT9_REFLECTION.md)

### Changelog
 - [CHANGELOG.md](CHANGELOG.md)

## Planned Features

* Submit news text or article links
* AI-based misinformation detection
* Credibility score output
* Simple user-friendly interface
* Storage of analyzed articles for reference

## Technologies (Planned)

* Frontend: Web Interface
* Backend: API Server
* AI Model: NLP-based classification
* Database: Article storage and results

# Language Choice and Design Decisions

### Programming Language Choice

This project was implemented in Python because it provides:

- Simple and readable syntax, making it ideal for rapid development
-Strong support for testing frameworks such as pytest
- Good structure for implementing design patterns
- Wide use in AI and data-driven applications

Python was selected to ensure maintainability and ease of testing throughout the development process.

### Key Design Decisions
#### 1. Object-Oriented Design

The system is structured using object-oriented principles to improve:

- Modularity
- Code reusability
- Maintainability

Core entities such as User, NewsArticle, and Result are represented as separate classes.

#### 2. Creational Design Patterns

Multiple creational patterns were implemented to demonstrate flexible object creation:

- Factory Method & Simple Factory → centralised object creation logic
- Abstract Factory → creation of related objects without specifying concrete classes
- Builder Pattern → step-by-step construction of complex objects
- Prototype Pattern → cloning existing objects efficiently
- Singleton Pattern → ensures a single shared instance where required

These patterns improve scalability and reduce tight coupling between components.

#### 3. Testing Strategy
- pytest was used for unit testing
- pytest-cov was used to measure test coverage
- Tests focus on verifying correctness of design pattern implementations

#### 4. Project Structure

The project is divided into:
- src/ → core application logic
- creational_patterns/ → design pattern implementations
- tests/ → unit tests
  
This separation ensures clarity and maintainability.

### Evidence
<img width="1643" height="766" alt="image" src="https://github.com/user-attachments/assets/cbcc6248-76fb-47de-a2f0-8a51a4b9c136" />

# Architecture Justification for Assignment 11
## Task 1: Repository Interface Design

The system uses a Repository Interface layer to decouple business logic from data access logic.

Each repository defines a clear contract (e.g., UserRepository, NewsArticleRepository) that specifies CRUD operations without exposing implementation details.

Why this approach was chosen:
Separation of concerns: Business logic does not depend on storage logic.
Testability: Repositories can be easily mocked or replaced in unit tests.
Flexibility: Enables swapping between in-memory, file-based, or database storage without modifying core logic.
Scalability: New data sources can be added by implementing the same interface.

This aligns with clean architecture principles and supports long-term maintainability.

## Task 3: Storage-Abstraction Mechanism (Dependency Injection vs Factory)

The system uses Dependency Injection (DI) rather than a Factory pattern for managing storage implementations.

Why Dependency Injection was chosen:
Loose coupling: Components receive dependencies externally instead of creating them internally.
Improved testability: Mock repositories can be injected during testing without modifying production code.
Flexibility in configuration: Storage type (e.g., in-memory, database) can be selected at runtime via configuration.
Better adherence to SOLID principles, especially:
D (Dependency Inversion Principle): High-level modules depend on abstractions, not concrete implementations.
Why not Factory Pattern:

While the Factory pattern centralizes object creation, it still introduces hidden coupling inside the factory, making runtime substitution and testing less flexible compared to DI.

## Task 4: Future-Proofing

The class diagram has been updated to include repository interfaces and their concrete implementations, ensuring improved extensibility, maintainability, and a clear separation between business logic and data access layers.

## REST API

This project uses FastAPI to expose RESTful API endpoints for managing users, articles, and analysis results.

Run the API server using:

```bash
uvicorn main:app --reload

```

## CRUD Endpoints

### Users
- GET `/api/users`
- POST `/api/users`
- PUT `/api/users/{id}`
- DELETE `/api/users/{id}`

### Articles
- GET `/api/articles`
- POST `/api/articles`
- PUT `/api/articles/{id}`
- DELETE `/api/articles/{id}`

### Results
- GET `/api/results`
- POST `/api/results`
- PUT `/api/results/{id}`
- DELETE `/api/results/{id}`

### Workflow Endpoint
- POST `/api/articles/{id}/analyze`

## Swagger Documentation

FastAPI automatically generates Swagger/OpenAPI documentation.

Open in browser:

http://127.0.0.1:8000/docs

## Testing

Testing was implemented using pytest and FastAPI TestClient.

The project includes:
- Repository unit tests
- Service layer tests
- API integration tests
- Coverage testing using pytest-cov

Run tests:

```bash
pytest

pytest --cov=services --cov=api --cov=repositories


```
## Architecture

The project follows a layered architecture:

```text
API Layer → Service Layer → Repository Layer
```
# Evidence
[Screenshots](screenshots.md)

## CI/CD Pipeline

This project uses GitHub Actions to automate testing and artifact generation.

### Continuous Integration (CI)
The CI pipeline automatically:
- Runs on every push
- Runs on pull requests to main
- Installs project dependencies
- Executes all unit and integration tests
- Runs coverage checks

### Continuous Deployment (CD)
When changes are merged into the main branch:
- A release artifact ZIP file is automatically generated
- The artifact is uploaded using GitHub Actions

The workflow configuration is located in:

.github/workflows/ci.yml

## Getting Started

### Prerequisites

- Python 3.13+
- FastAPI
- pytest
- pytest-cov

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI_Fake_News_Detector
```

Install dependencies:

```bash
pip install fastapi uvicorn pytest pytest-cov httpx
```

Run the application:

```bash
uvicorn main:app --reload
```

Run tests:

```bash
pytest
```
## Community Contributions

Contributors can participate by:

- Fixing bugs
- Adding tests
- Improving documentation
- Implementing new features
- Reviewing pull requests

See CONTRIBUTING.md for contribution guidelines.

Current contribution opportunities are available in GitHub Issues under:

- good-first-issue
- feature-request




