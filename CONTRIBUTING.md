# Contributing

Thank you for your interest in contributing to the AI-Powered Fake News Detection System.

## Prerequisites

Before contributing, ensure you have:

* Python 3.13+
* Git
* pytest
* FastAPI

## Installation

1. Fork the repository.
2. Clone your fork:

```bash
git clone <repository-url>
```

3. Install dependencies:

```bash
pip install fastapi uvicorn pytest pytest-cov httpx
```

## Running Tests

Run all tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov=services --cov=api --cov=repositories
```

## Coding Standards

* Follow Python naming conventions (PEP 8).
* Write meaningful commit messages.
* Add tests for new functionality.
* Ensure all tests pass before submitting a pull request.

## How to Contribute

1. Fork this repository.
2. Select an issue labeled `good-first-issue`.
3. Create a feature branch.
4. Implement your changes and tests.
5. Submit a pull request with a clear description.

## Pull Request Requirements

* All GitHub Actions checks must pass.
* Include relevant tests.
* Update documentation where necessary.
* Keep pull requests focused on a single feature or fix.

