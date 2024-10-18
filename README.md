# Time Tracking API

This project is a simple **Time Tracking API** built using **FastAPI** and **SQLAlchemy** to interact with a PostgreSQL database. The API allows users to create, retrieve, and filter time entries for specific dates and date ranges.

## Features

- **Create Time Entries:** Submit time entries including entry, lunch, and exit times.
- **Retrieve Time Entries:** Fetch time entries by specific dates or date ranges.
- **Filter Time Entries:** Retrieve entries greater than or equal to a specific date.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.12 or later
- PostgreSQL
- Virtual environment tools (optional but recommended)

## Installation

```bash
git clone https://github.com/LesterCerioli/CloudSuite-HR-Python312-BackEnd.git
cd time-tracking-api
```

## 2.Set up the Python environment
It's recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 3. Install the dependencies
After setting up the virtual environment, install the required packages:
```bash
pip install -r requirements.txt
```

## 4. Configure environment variables
Create a .env file in the root of your project and configure your PostgreSQL database credentials:
```bash
DATABASE_URL=postgresql://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
```

## 5. Run the Database Migrations
If you're using Alembic for database migrations, run:
```bash
alembic upgrade head
```

## 6. Start the FastAPI server
Run the server with the following command:
```bash
uvicorn app.main:app --reload
```

# API Endpoints
## 1. Create a Time Entry
### POST /times
Request Body:
```json
{
  "date": "2024-10-15",
  "entry_time": "2024-10-15T09:00:00",
  "lunch_entry_time": "2024-10-15T12:00:00",
  "lunch_exit_time": "2024-10-15T13:00:00",
  "exit_time": "2024-10-15T17:00:00"
}
```


