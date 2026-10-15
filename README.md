# Campus Desk

Portfolio project by Shagun Sharma. A Django course desk: students enroll while seats remain, and further sign-ups are waitlisted. Original sample code.

## Stack

Python, Django 5, SQLite by default, MySQL when `DB_ENGINE=mysql`.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Django==5.1.4
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

`mysqlclient` is listed for the MySQL option. The default path does not need it.

## Tests

```bash
python manage.py test
```

## Documents

System design, architecture, the database, the team plan, the delivery plan, and report notes are in `docs/`. Diagrams are in `docs/images/`.
