# syntax=docker/dockerfile:1

FROM python:3.11-alpine
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 8000
#https://stackoverflow.com/questions/60183313/the-connection-was-reset-in-localhost8000-using-django-and-docker
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
