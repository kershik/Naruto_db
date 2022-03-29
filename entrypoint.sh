#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$ENV" = "development" ]
then
    echo "Creating and filling tables with data..."
    python manage.py --seed
    echo "Tables created and filled."
fi

exec "$@"
