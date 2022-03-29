FROM python:3.10.2-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN pip install -r /usr/src/app/requirements.txt

COPY . usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
