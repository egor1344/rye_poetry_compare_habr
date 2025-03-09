build:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml build

up:
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build backend

local_load:
	docker compose -f docker-compose.load.yml run load k6 run --log-format json -q --console-output "loadtest.log" main.js

prod_load:
	docker compose -f docker-compose.load.yml run load k6 run  --log-format json -q main.js -o experimental-prometheus-rw

redis_up:
	docker-compose up redis

down:
	docker-compose down

exec_backend:
	docker-compose exec backend sh

pre_commit:
	# make pre_commit_clear
	make pre_commit_check

pre_commit_check:
	pre-commit run --all-files

pre_commit_clear:
	black --config backend/pyproject.toml backend/
	isort --sp backend/pyproject.toml backend/

shell:
	docker-compose exec backend python manage.py shell
