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
 - [CHANGELOG.md](./CHANGELOG.md)

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








