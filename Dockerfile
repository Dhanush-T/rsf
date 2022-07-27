FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    netcat \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.0.4"

COPY requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /app

COPY . .

ENTRYPOINT [ "/app/entrypoint.prod.sh" ]

CMD gunicorn rsf.wsgi:application --bind 0.0.0.0:8000
