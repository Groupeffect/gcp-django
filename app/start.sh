#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py setup
service nginx start 
# if $DEBUG = 1 then run the server in debug mode
if [ $DEBUG = 'True' ]; then
    python manage.py runserver 0.0.0.0:8000
else
    # gunicorn --bind $PORT /app/backend.wsgi:application --workers 3 --timeout 120 --log-level=debug
    gunicorn backend.wsgi:application --bind 0.0.0.0:8000
fi
