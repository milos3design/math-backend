#!/bin/sh

# Wait for PostgreSQL
if [ "$DATABASE_HOST" ] && [ "$DATABASE_PORT" ]; then
    echo "Waiting for Postgres..."
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done
    echo "Postgres started"
fi

# Run migrations
python manage.py migrate --noinput

exec "$@"
