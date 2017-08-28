FROM python:2.7

MAINTAINER john munyui gathure

ENV PYTHONUNBUFFERED 1

# Local copy of the project
ENV PROJECT_SRC=.

# directory in container for all project files
ENV SOURCE_DIR=/application

RUN mkdir $SOURCE_DIR
COPY $PROJECT_SRC $SOURCE_DIR

RUN pip install -r $SOURCE_DIR/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $SOURCE_DIR
ENTRYPOINT ["/application/docker-entrypoint.sh"]
