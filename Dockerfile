FROM python:3.10

WORKDIR /code/

# Use modern Poetry installer here
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /code/

# In production it may be better to avoid Poetry dependency
# and use exported requirements.txt as a source for Pip.
# Follow for example: https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry 
RUN poetry install

# RUN apt-get update && apt-get install -y \
#   postgresql-client \
#   redis-tools \
#   && rm -rf /var/lib/apt/lists/*


COPY . /code
ENV PYTHONPATH=/code/src
EXPOSE 8000