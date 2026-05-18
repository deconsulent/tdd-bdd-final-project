# TDD/BDD Final Project - Product Catalogue

This project implements a microservice-based product catalogue backend for an e-commerce application using Test Driven Development (TDD) and Behaviour Driven Development (BDD).

## Tech Stack
- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **factory_boy** - Test data generation
- **Behave** - BDD testing
- **Selenium** - UI automation

## Project Structure
```
.
├── service/
│   ├── __init__.py       # Flask app initialization
│   ├── models.py         # Product model
│   ├── routes.py         # REST API routes
│   ├── common/
│   │   └── status.py     # HTTP status codes
│   └── static/
│       └── index.html    # Admin UI
├── tests/
│   ├── factories.py      # ProductFactory (factory_boy)
│   ├── test_models.py    # TDD model tests
│   └── test_routes.py    # TDD route tests
├── features/
│   ├── products.feature  # BDD scenarios (Gherkin)
│   ├── environment.py    # Behave environment setup
│   └── steps/
│       ├── load_steps.py # BDD data loading steps
│       └── web_steps.py  # BDD Selenium web steps
├── config.py
└── requirements.txt
```

## Running the Service
```bash
pip install -r requirements.txt
python -m flask run
```

## Running TDD Tests
```bash
python -m pytest tests/ -v
```

## Running BDD Tests
```bash
behave
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | List all products |
| GET | /products?name=X | Search by name |
| GET | /products?category=X | Search by category |
| GET | /products?available=true | Search by availability |
| GET | /products/{id} | Read a product |
| POST | /products | Create a product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |
