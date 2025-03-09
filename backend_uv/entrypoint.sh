#!/bin/sh
uv run wait-for
uv run python manage.py migrate
exec "$@"
