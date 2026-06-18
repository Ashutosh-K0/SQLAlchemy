# SQLAlchemy Learning Repository

This repository contains small, focused examples that demonstrate different ways to work with SQLAlchemy using SQLite databases.

It covers:

- raw SQL execution through SQLAlchemy
- SQLAlchemy Core table and query operations
- SQLAlchemy ORM models and CRUD
- joins and aggregations with related tables

## Project Structure

- `basics.py`: Engine, connection, session, raw SQL `CREATE`, `INSERT`, and `SELECT`
- `core.py`: SQLAlchemy Core with `MetaData`, `Table`, `Insert`, `Update`, `Delete`, and `Select`
- `orm.py`: ORM models with `declarative_base`, relationships, and session-based CRUD
- `relationship.py`: Core-based relationship examples with `JOIN` and `GROUP BY` aggregations
- `requirements.txt`: Python environment dependencies (currently broader than this demo project)

## Prerequisites

- Python 3.10+
- pip

## Setup

1. (Optional) create and activate a virtual environment:

	Windows PowerShell:

	```powershell
	python -m venv myenv
	.\myenv\Scripts\Activate.ps1
	```

2. Install dependencies:

	```powershell
	pip install sqlalchemy
	```

	If you want to install everything listed in this repository:

	```powershell
	pip install -r requirements.txt
	```

## Run Examples

Run each script directly:

```powershell
python basics.py
python core.py
python orm.py
python relationship.py
```

Because `echo=True` is enabled in all scripts, SQL statements are printed to the console so you can see exactly what SQLAlchemy is sending to SQLite.

## What Each Script Does

### 1) basics.py

- Connects to `mydatabase.db`
- Creates `people` table if it does not exist
- Inserts one row
- Reads and prints all rows

### 2) core.py

- Connects to `core_database.db`
- Defines `people` and `things` tables with `MetaData`
- Creates tables via `meta.create_all(engine)`
- Demonstrates insert, update, delete, and select operations using Core expressions

### 3) orm.py

- Connects to `example.db`
- Defines ORM classes `Person` and `Thing` with a one-to-many relationship
- Creates tables via `Base.metadata.create_all(engine)`
- Includes commented examples for insert/select/delete
- Runs an update example that renames `Charlie` to `Charles`

### 4) relationship.py

- Connects to `relationship_database.db`
- Defines related `people` and `things` tables
- Includes commented bulk inserts for sample data
- Demonstrates:
  - `JOIN` between people and things
  - `GROUP BY` with `SUM(value)` by owner

## Notes

- Running scripts multiple times can add duplicate data unless rows are cleaned or insert logic is guarded.
- `relationship.py` has sample insert blocks commented out. Uncomment them once to seed data before running join/group queries.
- Database files (`*.db`) are created automatically in the project folder.

## Learning Tips

- Start with `basics.py`, then move to `core.py`, `relationship.py`, and finally `orm.py`.
- Compare the SQL output (`echo=True`) to your Python code to build intuition.
- Try changing filters/values and rerun scripts to observe behavior.
