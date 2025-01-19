#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then 
  echo "Checking if database is running"

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "The database is up and running"
fi


python manage.py migrate

python manage.py runserver 0.0.0.0:8000

exec "$@"
