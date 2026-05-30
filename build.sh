#!/usr/bin/env bash
set -euo pipefail

pip install --upgrade pip
pip install -r requirements.txt

export DJANGO_SECRET_KEY="${DJANGO_SECRET_KEY:-build-time-secret-key}"
python manage.py collectstatic --noinput
