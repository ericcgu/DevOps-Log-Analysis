#!/bin/sh
echo "Waiting for PostgreSQL..."
while ! nc -z postgresql 5432; do
    sleep 0.1
done
echo "PostgreSQL Started"
python app.py