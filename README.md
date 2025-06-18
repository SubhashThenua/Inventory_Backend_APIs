Here's a well-maintained, comprehensive `README.md` for your Inventory Management API:

```markdown
# Inventory Management API

A robust inventory management system with JWT authentication, built with FastAPI and MySQL.

## ✨ Features

-  JWT Authentication (Login/Register)
-  Product Add, Update and GET Operations
-  Inventory quantity management
-  MySQL database 
-  Request validation
-  Comprehensive error handling
-  Database initialization script
- 🔄 Automatic API documentation (Swagger/ReDoc)

## 📚 API Documentation

After starting the server, access interactive documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Base URL
`http://127.0.0.1:8000`

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- MySQL Server
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/inventory-api.git
   cd inventory-api
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL Database**
   ```bash
   sudo service mysql start  # Linux
   mysql -u root -p -e "CREATE DATABASE inventory_db;"
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=inventory_db
   SECRET_KEY=your_random_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. **Initialize database**
   ```bash
   python initial_data.py
   ```

7. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## 🛠️ API Endpoints

### Authentication

| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| POST   | `/register` | Register new user    |
| POST   | `/login`    | Login and get JWT token |

### Products

| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| GET    | `/products/`    | List all products (paginated) |
| POST   | `/products/`    | Create new product   |
| GET    | `/products/{id}`| Get product details  |
| PUT    | `/products/{id}/quantity`| Update product Quantity      |



```
