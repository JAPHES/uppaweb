"""
Production-ready Django settings for uppawebsite.
Optimised for Railway deployment with Gunicorn and WhiteNoise.
"""
import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


def env_list(name):
    return [item.strip() for item in os.getenv(name, "").split(",") if item.strip()]

# ----------------------------------------------------------------------------
# Core settings
# ----------------------------------------------------------------------------
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

# Secret key: required in production, fallback only for local dev.
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or os.getenv("SECRET_KEY") or "dev-secret-key"
if not DEBUG and SECRET_KEY == "dev-secret-key":
    raise RuntimeError("DJANGO_SECRET_KEY or SECRET_KEY must be set in production")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "healthcheck.railway.app"]
railway_public_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if railway_public_domain:
    ALLOWED_HOSTS.append(railway_public_domain)
ALLOWED_HOSTS.extend(env_list("DJANGO_ALLOWED_HOSTS"))

default_csrf_origins = set()
if railway_public_domain:
    default_csrf_origins.add(f"https://{railway_public_domain}")
csrf_env = os.getenv("CSRF_TRUSTED_ORIGINS", "")
if csrf_env:
    default_csrf_origins.update(origin.strip() for origin in csrf_env.split(",") if origin.strip())
CSRF_TRUSTED_ORIGINS = sorted(default_csrf_origins)

# ----------------------------------------------------------------------------
# Applications
# ----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "uppa",
]

# ----------------------------------------------------------------------------
# Middleware
# ----------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "uppawebsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "uppawebsite.wsgi.application"

# ----------------------------------------------------------------------------
# Database
# - Local: SQLite (no sslmode, avoids crashes)
# - Production: DATABASE_URL (e.g., Postgres on Railway) with SSL required by default
# ----------------------------------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_SSL_REQUIRE = os.getenv("DATABASE_SSL_REQUIRE", "true").lower() == "true"
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=DATABASE_SSL_REQUIRE,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ----------------------------------------------------------------------------
# Password validation
# ----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------------------------------------------------------
# Internationalization
# ----------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------------------------------
# Static files (served by WhiteNoise in production)
# ----------------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"              # collectstatic target
STATICFILES_DIRS = [BASE_DIR / "uppa" / "static"]   # source assets

STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

# ----------------------------------------------------------------------------
# Security hardening
# ----------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ----------------------------------------------------------------------------
# Defaults
# ----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
