# Sanic Clean Architecture

An educational user API built with [Sanic](https://sanic.dev/) and organized
using Clean Architecture principles. The project keeps business rules
independent from the web framework and storage implementation, making each
layer easier to understand, test, and replace.

> This is a learning project. User data is stored in memory and is lost when
> the application stops.

## Features

- Sanic-based asynchronous HTTP API
- Clean separation between domain, application, presentation, and
  infrastructure layers
- Dependency injection at the application composition root
- Pydantic request and response validation
- In-memory user repository
- Unit test for the create-user use case

## Requirements

- Python 3.11 or newer
- `pip`

## Installation

Clone the repository and create a virtual environment:

```powershell
git clone https://github.com/manojtharindu11/sanic-learning.git
cd sanic-learning
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell does not allow script execution, activate the environment using
the command appropriate for your shell or run the project through the
environment's Python executable directly.

## Running the API

Start the development server with:

```powershell
sanic-clean-architecture
```

Alternatively, run the server module directly:

```powershell
python src\server.py
```

The API listens on `http://127.0.0.1:8000`.

## API

### Health-style greeting

```http
GET /api/v1/users/hello
```

Example response:

```json
{
  "message": "Hello User"
}
```

### Create a user

```http
POST /api/v1/users/
Content-Type: application/json
```

Example request:

```json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "age": 36
}
```

Example response:

```json
{
  "id": 1,
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "age": 36
}
```

Validation rules:

- `name` must contain between 2 and 100 characters
- `email` must be a valid email address
- `age` must be at least 18

Using `curl` from PowerShell:

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/v1/users/ `
  -H "Content-Type: application/json" `
  -d '{\"name\":\"Ada Lovelace\",\"email\":\"ada@example.com\",\"age\":36}'
```

## Architecture

The dependency direction is kept inward:

```text
presentation -> application -> domain
infrastructure -> domain
```

### Domain

`src/domain/` contains the framework-independent `User` entity and repository
contract. It does not depend on Sanic, Pydantic, or a specific storage engine.

### Application

`src/application/` contains the `CreateUser` use case and its command object.
The use case coordinates the operation through the repository abstraction.

### Presentation

`src/presentation/` contains Sanic routes and Pydantic HTTP schemas. Request
validation stays at the API boundary rather than leaking into the domain.

### Infrastructure

`src/infrastructure/` contains concrete adapters, currently an
`InMemoryUserRepository`. A database-backed implementation can replace it
without changing the use case.

### Composition root

`src/app.py` creates the repository, injects it into the use case, and injects
the use case into the route factory. This keeps route handlers independent from
concrete storage.

## Running tests

```powershell
pytest
```

## Project layout

```text
.
├── src/
│   ├── application/       # Use cases and application commands
│   ├── domain/             # Entities and repository contracts
│   ├── infrastructure/    # Concrete adapters
│   ├── presentation/      # HTTP routes and Pydantic schemas
│   ├── app.py              # Application composition root
│   └── server.py           # Development server entry point
├── tests/                  # Automated tests
└── pyproject.toml          # Project metadata and dependencies
```

## Extending the repository

To use persistent storage:

1. Implement `domain.repositories.user_repository.UserRepository`.
2. Add the adapter under `src/infrastructure/`.
3. Replace `InMemoryUserRepository` in `src/app.py`.

The `CreateUser` use case and HTTP routes can remain unchanged.

## License

No license has been declared yet. Add a license before distributing this
project or accepting external contributions.
