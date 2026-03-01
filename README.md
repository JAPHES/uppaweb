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

## Deployment Notes
- This project is configured for deployment with `gunicorn` and `whitenoise`.
- `ALLOWED_HOSTS` currently includes:
  - `uppawebsite.onrender.com`
  - `127.0.0.1`
  - `localhost`

## Important
- `DEBUG` is currently enabled in settings.  
  Set `DEBUG = False` before production deployment.
