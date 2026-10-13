# AVANTOPS AI Backend

## Environment

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## API docs

- http://localhost:8000/docs

## Key features

- auth endpoints
- trading signal endpoints
- portfolio endpoints
- subscriptions skeleton
- risk + strategy services
