# Overcloaking Django

## ENV

```
SITE_HOST=localhost
DEBUG=False
API_DOCS_ENABLE=False

# Если есть mkcert, то можете прокинуть свои локальные сертификаты в nginx,
# тем самым подняв https соединение на локалке. Если не хочется этим заниматься,
# то поставьте переменную TLS_MODE=off, и заходите на проект по http://localhost:8000
TLS_MODE=off
ADMIN_HTPASSWD=admin:{PLAIN}admin
TLS_CERTIFICATE=.certs/localhost.pem
TLS_CERTIFICATE_KEY=.certs/localhost-key.pem

SECRET_KEY=my_very_sercet_key

POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_NAME=postgres
POSTGRES_USER=postgres

```

## Локальная сборка приложений

```shell
docker-compose build
```

## Локальный запуск poetry

```shell
docker-compose run --rm backend_poetry
```

## Локальный запуск uv

```shell
docker-compose run --rm backend_uv
```

## Локальный запуск poetry

```shell
docker-compose run --rm backend_rye
```