# FastAPI Project Template

A  FastAPI project template with Docker support.

## Project Structure

```
├── app/                      # Main application package
│   ├── __init__.py
│   ├── main.py              # FastAPI application instance and configurations
│   ├── api/                 # API endpoints
│   │   ├── __init__.py
│   │   ├── v1/             # API version 1
│   │   │   ├── __init__.py
│   │   │   └── router.py   # API v1 endpoints
│   ├── core/               # Core application components
│   │   ├── __init__.py
│   │   └── config.py      # Configuration settings
│   ├── models/            # Pydantic models for data validation
│   │   ├── __init__.py
│   │   └── item.py       # Example Item model
│   └── schemas/          # Database models (if using ORM)
│       ├── __init__.py
│       └── item.py
├── tests/               # Test directory
│   ├── __init__.py
│   └── test_api.py     # API tests
├── .env.example        # Example environment variables
├── .gitignore         # Git ignore file
├── docker-compose.yml # Docker Compose configuration
├── Dockerfile        # Docker build instructions
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Key Components

### Configuration Files
- `Dockerfile`: Defines the container build process
- `docker-compose.yml`: Defines services, networks, and volumes
- `.env.example`: Template for environment variables
- `requirements.txt`: Python package dependencies

### Application Code
- `app/main.py`: Application entry point and FastAPI setup
- `app/core/config.py`: Configuration management using Pydantic
- `app/api/v1/router.py`: API endpoints implementation
- `app/models/`: Pydantic models for request/response validation

### Tests
- `tests/test_api.py`: Example API tests using pytest

## Setup and Running

### Prerequisites
- Python 3.11+
- Docker and Docker Compose

### Local Development Setup


1. Build and run using Docker Compose:
```bash
docker-compose up --build
```

## API Documentation

Once running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

### API v1

- `GET /api/v1/items/`: List all items
- `POST /api/v1/items/`: Create a new item
- `GET /`: Root endpoint (health check)

## Testing

Run tests using pytest:
```bash
pytest
```

## Project Features

- ✅ FastAPI with Python 3.11
- ✅ Pydantic data validation
- ✅ API versioning
- ✅ Docker support
- ✅ Environment variables configuration
- ✅ Test setup with pytest
- ✅ Example CRUD operations
- ✅ Clear project structure
