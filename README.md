# A simple fastapi api notes.

## Steps to use the api

1. **Install all dependencies**:
```
pip install -r requirements.txt
```

2. **From the root of the project, execute**:
```
uvicorn backend.main/app --reload
```

The server will run on
- http://127.0.0.1:8000

3. **Automatic documentation**

FastAPI provides interactive documentation:
- Swagger UI -> http://127.0.0.1:8000/docs
- ReDoc -> http://127.0.0.1:8000/redoc