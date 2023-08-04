#It instructs Docker Engine to use official python:3.8 as the base image
FROM python:3.8.13

ARG APP=/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#It creates a working directory(app) for the Docker image and container
WORKDIR ${APP}

RUN apt-get update && apt-get install -y locales --no-install-recommends \
    vim && \
    sed -i -e 's/# es_MX.UTF-8 UTF-8/es_MX.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG es_MX.UTF-8
ENV LC_ALL es_MX.UTF-8

ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# It copies the framework and the dependencies 
# for the FastAPI application into the working directory
COPY requirements.txt .

# It will install the framework and the dependencies
# in the `requirements.txt` file.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# It will copy the remaining files and the source code from the host
# `fast-api` folder to the `app` container working directory
COPY . ${APP}

#It will expose the FastAPI application on port `8000` inside the container
EXPOSE 8000

#It is the command that will start and run the FastAPI application container
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod u+x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]