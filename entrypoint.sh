#!/bin/bash

DB_NAME=db
DB_PORT=5432

for _ in `seq 0 100`; do
    (echo > /dev/tcp/${DB_NAME}/${DB_PORT}) >/dev/null 2>&1
    if [[ $? -eq 0 ]]; then
        break
    fi
    sleep 1
done

python manage.py migrate && python manage.py runserver 0.0.0.0:8000
