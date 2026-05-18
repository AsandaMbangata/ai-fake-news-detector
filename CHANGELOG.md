# Changelog

### Added
- Implemented all creational design patterns:
  - Simple Factory
  - Factory Method
  - Abstract Factory
  - Builder
  - Prototype
  - Singleton
- Added core domain models (User, NewsArticle, Result)
- Added unit tests for Singleton and Prototype
- Added initial project structure

### Fixed
- Fixed Singleton test cases (instance consistency)
- Fixed import issues across test modules

### Testing
- Added pytest unit tests
- Configured coverage reporting (pytest-cov)
- Achieved working test suite execution

### GitHub
- Linked commits to issues using `Fix #ID` format
- Cleaned repository structure and added `.gitignore`
- Removed `__pycache__` and `.coverage` files from tracking

## Repository Layer Update
- Added repository abstraction layer
- Added in-memory repositories for User, Article, and Result
- Added CRUD operations
- Added repository unit tests
- Added future database repository stubs
- Improved project structure and maintainability

## Assignment 12 Update
### Added
- Service layer architecture
- REST API using FastAPI
- CRUD API endpoints
- Article analysis workflow endpoint
- API integration tests
- Swagger/OpenAPI documentation

### Improved
- Repository abstraction
- Layered application architecture
- Test coverage
