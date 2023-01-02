FROM python:3.10-slim
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip3 install locust

ENTRYPOINT ["locust --users 10 --spawn-rate 1 -H backend"]
