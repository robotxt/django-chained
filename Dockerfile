FROM python:3.11-slim-bullseye AS base

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install -y libpq-dev gdal-bin gcc
RUN pip install --upgrade pip poetry setuptools

# create user and make the app dir the working directory
RUN useradd -m -d /appuser/ appuser

FROM base AS django 

WORKDIR /app

# copy environment to the container
COPY . /app
COPY pyproject.toml poetry.lock /app/
COPY scripts/gunicorn.sh /

# install python dependencies
RUN poetry cache clear --all pypi
RUN poetry config virtualenvs.create false && poetry update
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

WORKDIR /app/web/

CMD ["/gunicorn.sh"]
