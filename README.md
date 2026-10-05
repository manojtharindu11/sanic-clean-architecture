# Sanic Clean Architecture

This project separates business rules from delivery and implementation details.
Application code lives in the `src/` package tree:

```text
presentation -> application -> domain
infrastructure -> domain
```

The arrows show the allowed dependency direction. The domain has no Sanic,
Pydantic, or storage dependency.

## Layers

- **Domain** (`src/domain/`): business entities and repository ports. These are
  framework-independent contracts.
- **Application** (`src/application/`): use cases and application commands. A use
  case coordinates domain behavior through ports.
- **Presentation** (`src/presentation/`): Sanic routes and HTTP request/response
  schemas. Pydantic validation belongs here because it is an API concern.
- **Infrastructure** (`src/infrastructure/`): concrete adapters such as the
  in-memory repository. A database adapter can replace it without changing
  the use case.

## Dependency injection

`src/app.py` is the composition root. It creates the concrete repository, injects
it into `CreateUser`, and injects that use case into the route factory. Routes
therefore do not construct repositories or depend on concrete storage.

To use a different repository, implement
`domain.repositories.user_repository.UserRepository` and
change only the composition in `src/app.py`.

## Running

```powershell
.\.venv\Scripts\sanic-clean-architecture.exe
```

The API is available at `http://127.0.0.1:8000`.
