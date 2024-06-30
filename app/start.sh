#!/bin/bash
python /app/manage.py makemigrations
python /app/manage.py migrate
python /app/manage.py setup
service nginx start 
# if $DEBUG = 1 then run the server in debug mode
if [ $DEBUG = 1 ]; then
    python /app/manage.py runserver 0.0.0.0:$PORT
else
    gunicorn --bind $PORT /app/backend.wsgi:application --workers 3 --timeout 120 --log-level=debug --log-file=-
fi
