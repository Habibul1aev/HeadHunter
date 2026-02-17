FROM python:3.11-alpine3.16

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    postgresql-client \
    postgresql-dev \
    build-base

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]