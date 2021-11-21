#!/bin/sh

echo "Waiting for postgres..."

# scan for web-db at port 5432
while ! nc -z web-db 5432; do
	sleep 0.1
done

echo "PostgreSQL started"

# this accepts any command passed onto the script call
exec "$@"


