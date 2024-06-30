#!/bin/bash
rm -drf /app/api/migrations
rm /app/db.sqlite3
mkdir -p /app/api/migrations
touch /app/api/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
python /app/manage.py setup

