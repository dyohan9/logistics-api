FROM python:3.6-alpine3.7

ENV WORKDIR /home/app
WORKDIR $WORKDIR

RUN apk update && apk add alpine-sdk postgresql-dev

RUN pip install pipenv
RUN pip install gunicorn
RUN pip install gevent
RUN pip install psycopg2-binary

COPY . .

RUN pipenv install --system

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]