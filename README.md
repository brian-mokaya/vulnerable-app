# Ripple Demo API

This repository is a deliberately small FastAPI application used as a realistic demo target for the Ripple hackathon project.

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pytest
- Python logging
- Environment variables

## Endpoints

- `GET /`
- `GET /health`
- `POST /login`
- `GET /users`

## Health behavior

The app currently expects `DATABASE_URL` to be present. When it is set, `GET /health` returns:

```json
{
	"status": "healthy",
	"database": "connected"
}
```

When `DATABASE_URL` is missing, it returns:

```json
{
	"status": "degraded",
	"database": "unavailable"
}
```

The intended demo failure later is simple: change the app to look for `DB_URL` while the environment still only provides `DATABASE_URL`. That makes the health check degrade immediately and is easy for judges to understand.

## Run locally

1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Copy `.env.example` to `.env` and set `DATABASE_URL`.
3. Start the app with:

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

## Tests

Run:

```bash
pytest
```

## Logging

Local logs are written to `logs/app.log` and include:

- app startup
- missing database configuration
- failed health checks
- failed login requests
