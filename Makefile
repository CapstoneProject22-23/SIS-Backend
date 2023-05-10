.PHONY: run-server
run-server:
	poetry run python -m  backend.manage runserver

.PHONY: migrations
migrations:
	poetry run python -m backend.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m backend.manage migrate

.PHONY: install
install:
	poetry install

.PHONY: superuser
superuser:
	poetry run python -m backend.manage createsuperuser

.PHONY: update
update: install migrate ;