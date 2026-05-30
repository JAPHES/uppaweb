# UPPA Website

Official website project for **Universal Project Partnership Association (UPPA)**, built with Django.

## Tech Stack
- Python 3.13.3
- Django 5.2.3
- Bootstrap 5
- Font Awesome

## Project Structure
```text
uppaweb/
  manage.py
  requirements.txt
  runtime.txt
  .python-version
  railway.json
  uppa/                    # Main app (views, urls, templates, static)
    templates/uppa/        # Page templates
    static/                # App static assets
  uppawebsite/             # Django project config
  staticfiles/             # Collected static files (deployment)
```

## Main Pages
- `/` - Home
- `/about/` - About Us
- `/departments/` - Departments
- `/projects/` - Projects
- `/team/` - Team
- `/contact/` - Contact

## Local Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start development server:
   ```bash
   python manage.py runserver
   ```
5. Open `http://127.0.0.1:8000/`.

## Static Files
- App static assets are in `uppa/static/`.
- `STATIC_URL` is `/static/`.
- `STATICFILES_DIRS` includes `uppa/static`.
- For production:
  ```bash
  python manage.py collectstatic
  ```

## Railway Deployment
This project is configured for Railway with `railway.json`, `gunicorn`, and `whitenoise`.

Railway commands:
- Build command: `bash build.sh`
- Pre-deploy command: `python manage.py migrate --noinput`
- Start command: `gunicorn uppawebsite.wsgi:application --bind 0.0.0.0:$PORT --log-file -`

Required Railway variables:
- `DJANGO_SECRET_KEY`: a secure Django secret key
- `DATABASE_URL`: use the Railway Postgres variable reference, for example `${{Postgres.DATABASE_URL}}`
- `DJANGO_DEBUG`: set to `False`

Optional variables:
- `DJANGO_ALLOWED_HOSTS`: comma-separated extra domains, for custom domains
- `CSRF_TRUSTED_ORIGINS`: comma-separated origins such as `https://example.com`
- `DATABASE_SSL_REQUIRE`: defaults to `true`; set to `false` only for a non-SSL database

Railway health checks use `/health/` and the `healthcheck.railway.app` hostname.

Deploy from GitHub:
1. Push this repository to GitHub.
2. In Railway, create a new project and choose **Deploy from GitHub repo**.
3. Add a PostgreSQL service in the same Railway project.
4. In the app service variables, set `DJANGO_SECRET_KEY`, `DATABASE_URL`, and `DJANGO_DEBUG`.
5. Generate a public Railway domain from the app service Networking tab.
6. Redeploy the app service and check the deployment logs.

## Important
- Keep `DJANGO_DEBUG=False` in production.
- Do not rely on the checked-in SQLite database for production data; use Railway Postgres.
