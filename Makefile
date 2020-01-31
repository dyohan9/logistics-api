ENVIRONMENT_VARS_FILE := .env
CHECK_ENVIRONMENT := true


# Commands

help:
	@cat Makefile-help.txt
	@exit 0

check_environment:
	@if [ ${CHECK_ENVIRONMENT} = true ]; then make _check_environment; fi

install_requirements:
	@make install_development_requirements

lint:
	@PIPENV_DONT_LOAD_ENV=1 pipenv run flake8
	@echo "${SUCCESS}✔${NC} The code is following the PEP8"

test: check_environment
	@make migrate CHECK_ENVIRONMENT=false
	@make collectstatic CHECK_ENVIRONMENT=false
	@PIPENV_DONT_LOAD_ENV=1 SECRET_KEY=SK pipenv run coverage run manage.py test
	PIPENV_DONT_LOAD_ENV=1 pipenv run coverage report -m;

migrate:
	@make check_environment
	@pipenv run python manage.py migrate

start:
	@make check_environment
	@make migrate CHECK_ENVIRONMENT=false
	@make collectstatic CHECK_ENVIRONMENT=false
	@pipenv run python ./manage.py runserver

migrations:
	@make check_environment
	@pipenv run python ./manage.py makemigrations
	@make migrate CHECK_ENVIRONMENT=false

collectstatic:
	@make check_environment
	@pipenv run python manage.py collectstatic --no-input


# Utils

## Colors
SUCCESS = \033[0;32m
INFO = \033[0;36m
WARNING = \033[0;33m
DANGER = \033[0;31m
NC = \033[0m

create_environment_vars_file:
	@echo "SECRET_KEY=SK" > "${ENVIRONMENT_VARS_FILE}"
	@echo "DEBUG=true" >> "${ENVIRONMENT_VARS_FILE}"
	@echo "${SUCCESS}✔${NC} Settings file created"

install_development_requirements:
	@echo "${INFO}Installing development requirements...${NC}"
	@pipenv install --dev
	@echo "${SUCCESS}✔${NC} Development requirements installed"


# Checkers

_check_environment:
	@type pipenv || (echo "${DANGER}☓${NC} Install pipenv to continue..." && exit 1)
	@echo "${SUCCESS}✔${NC} pipenv installed"
	@if [ ! -f "${ENVIRONMENT_VARS_FILE}" ]; \
		then make create_environment_vars_file; \
	fi
	@make install_requirements
	@echo "${SUCCESS}✔${NC} Environment checked"