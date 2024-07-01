PROJECT_NAME=gcp-django
REPO_PATH=~/apps/groupeffect/github/$(PROJECT_NAME)
APP_NAME=app
CONTAINER_NAME=$(PROJECT_NAME)_web
APP_PATH=$(REPO_PATH)/$(APP_NAME)
UPDATE_TIME=$(shell date)

push:
	cd $(REPO_PATH)
	git add .
	git commit -m "update and build at $(UPDATE_TIME)"
	git push	

bash:
	podman exec -it $(CONTAINER_NAME)_1 bash

commit_container:
	podman commit $(CONTAINER_NAME)_1 $(CONTAINER_NAME):latest

build:
	podman-compose up --build --remove-orphans

up:
	podman-compose up

down:
	podman-compose down