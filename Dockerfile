FROM python:3.12.4-slim-bookworm AS base
ARG PORT=8080
ENV PORT=$PORT
ARG HOST=0.0.0.0
ENV HOST=$HOST
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends nginx
WORKDIR /app
COPY ./app/. .
COPY ./server/nginx/default.conf /etc/nginx/config.d/default.conf
RUN pip install -r requirements.txt
EXPOSE $PORT
EXPOSE 8000

FROM base AS prod
CMD bash /app/start.sh

