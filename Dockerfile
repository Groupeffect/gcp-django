FROM python:3.12.4-slim-bookworm AS base
ARG PORT=8080
ENV PORT=$PORT
ARG HOST=0.0.0.0
ENV HOST=$HOST
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx

RUN mkdir /app
WORKDIR /app
COPY app/. /app/.
COPY server/nginx/default.conf /etc/nginx/conf.d/default.conf
RUN pip install -r requirements.txt
EXPOSE $PORT
EXPOSE 8000

FROM base AS prod
CMD bash start.sh

