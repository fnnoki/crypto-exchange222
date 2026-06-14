# SQLite: use --workers 1 to avoid "database locked" errors
# PostgreSQL: --workers 2 is fine
web: uvicorn main:app --host 0.0.0.0 --port $PORT
