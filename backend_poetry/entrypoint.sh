#!/bin/sh
eval $(poetry env activate)
poetry run wait-for
poetry run python manage.py migrate
exec "$@"
