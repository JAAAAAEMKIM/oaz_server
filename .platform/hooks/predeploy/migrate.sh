#!/bin/bash
source /var/app/venv/*/bin/activate
python manage.py makemigrations --merge
python manage.py migrate --noinput
