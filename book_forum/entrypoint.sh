#!/bin/sh

poetry run python manage.py collectstatic;
poetry run python manage.py migrate;
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000