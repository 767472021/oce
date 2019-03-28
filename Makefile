help:
	@echo "server           run dev server"
	@echo "doc              run doc server"
	@echo "shell            open a python shell"
	@echo "mkmigrate        makemigrations"
	@echo "migrate          migrate"
	@echo "clean            clean"
	@echo "lint             run flake8 check"
	@echo "test             py.test --cov=. tests/"

server:
	@rm -rf /tmp/mako_tmp_oce/*
	@python manage.py runserver 0.0.0.0:5001

shell:
	@python manage.py shell

mkmigrate:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

clean: clean-build clean-pyc
	@rm -fr cover/

pytest:
	@py.test --cov=. --cov-report term-missing:skip-covered tests/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type f -name '*~' -delete
	@find . -type f -name '*,cover' -delete

lint:
	@flake8 . --exclude=.venv,migrations

doc:
	@mkdocs serve

.PHONY: server shell clean clean-build clean-pyc lint migrate mkmigrate
