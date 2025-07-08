### ▶️: Run the app

- If you're inside a virtual environment or uvicorn is not in your global PATH, run it like this:   `python -m uvicorn main:app --reload`

- After running, open your browser at:
    - http://127.0.0.1:8000
    - http://127.0.0.1:8000/docs  ← Swagger UI



`uvicorn main:app --reload`

- `main:app` → `main.py` and `app` inside it.
- `--reload` → Enables hot reloading during development.