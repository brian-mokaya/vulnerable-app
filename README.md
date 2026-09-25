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

1. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Set the environment variable the app expects.

```bash
cp .env.example .env
export DATABASE_URL=demo://connected
```

4. Start the server.

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

5. Confirm the app is running.

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

6. Try the login endpoint.

```bash
curl -X POST http://127.0.0.1:8000/login \
	-H "Content-Type: application/json" \
	-d '{"username":"demo","password":"ripple"}'
```

7. Check the users endpoint.

```bash
curl http://127.0.0.1:8000/users
```

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
