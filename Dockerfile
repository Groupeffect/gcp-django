FROM python:3.12.4-slim-bookworm
ARG PORT=8080
ENV PORT=$PORT
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./app/. .
RUN ls -a
RUN pip install -r requirements.txt
CMD python manage.py runserver "0.0.0.0:$PORT"