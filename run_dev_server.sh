#!/bin/sh

docker-compose --file docker-compose.dev.yml up -d 
WORKDIR="book_forum"
cd $WORKDIR
export ENV_FILE=".env.dev"
poetry run python manage.py runserver