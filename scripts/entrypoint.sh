#!/bin/sh
# set -e
python3 manage.py collectstatic --noinput

uwsgi --socket :8000 --master --processes 5 --threads 4 --enable-threads --buffer-size=55535 --module gqltest.wsgi