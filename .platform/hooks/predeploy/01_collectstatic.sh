#!/bin/sh
source /var/app/venv/*/bin/activate
cd /var/app/current
python manage.py collectstatic --noinput
    