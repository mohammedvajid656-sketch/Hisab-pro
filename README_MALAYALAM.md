# HisabPro — Django Accounting SaaS Starter

HisabPro is a beginner-friendly Django starter project for a multi-business accounting web application.

## What is included now
- User registration, login and logout (Django authentication)
- Each user can create multiple business workspaces
- Income and expense transaction entry
- Dashboard totals: income, expenses, net balance and number of entries
- Transaction list
- English / Malayalam language-link foundation
- Mobile responsive HTML/CSS
- SQLite database for local development
- Django admin registration for Business and Transaction

## Important limitations
This is a learning MVP, not production-ready accounting software. It currently uses simple income-minus-expense totals, not full double-entry bookkeeping. It does not yet include invoices, GST calculations, bank reconciliation, subscriptions, audit trails, role permissions, automated backups, or deployment hardening. Do not enter real sensitive financial data until these features and a security review are completed.

## Run locally
Use Python 3.10+ for this Django 5.2 starter.

```bash
python -m venv .venv
```

Activate the environment:

Linux/macOS:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\\Scripts\\activate
```

Install dependencies and create the database:
```bash
python -m pip install -r requirements.txt
python manage.py makemigrations accounting
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. Create a user, then create a business workspace. The admin is at `/admin/`.

## Android
A phone browser can access the app only while the Django server or a hosted development environment is running. A single HTML preview is not enough for Django. A cloud IDE with terminal support is often the easiest mobile-only workflow. Do not expose Django's development server directly to the public internet.

## Security before production
- Replace `SECRET_KEY` with an environment variable and set `DEBUG = False`.
- Set `ALLOWED_HOSTS` to the real domain only.
- Use HTTPS, secure cookies, PostgreSQL, a managed secret store and automated encrypted backups.
- Add automated tests for tenant isolation, accounting totals and permissions.
- Add audit logs and review the accounting/tax rules with a qualified professional.
