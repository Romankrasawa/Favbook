###########
# BUILDER #
###########

# pull official base image
FROM python:3.11

# set work directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update \
    && apt-get install -y postgresql

# install dependencies
COPY ./poetry.lock .
COPY ./pyproject.toml .
RUN pip install "poetry"
RUN poetry install 

# copy project
COPY . .
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]