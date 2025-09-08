
# 📚 Shofy Catalog API


### 1. Clone the project

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

Visit the docs at:  
📘 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker

### 1. Build and run

```bash
docker-compose up --build
```

## 🧪 Run Tests

> Run from project root (where the `app/` folder exists):

### ✅ Linux/macOS:

```bash
PYTHONPATH=. pytest
```

### ✅ Windows PowerShell:

```powershell
$env:PYTHONPATH = "."; pytest
```

---

## 📂 Folder Structure

```
Shofy_catalog/
├── app/
│   ├── api/v1/           # API routes
│   ├── core/             # DB connection
│   ├── crud/             # DB logic
│   ├── services/         # Business logic
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # Entry point
├── tests/                # Unit + API tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Author

Md. Abin Hasan

---
