FROM python:3.8

WORKDIR /app

RUN apt-get update -y

RUN apt-get install python3-dev -y

COPY ./requirements.txt requirements.txt
COPY ./igaworks .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate --settings=config.settings.production

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.production"]

EXPOSE 8000
