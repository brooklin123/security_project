FROM locustio/locust
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip3 install some-python-package
EXPOSE 8089
ENTRYPOINT ["-f","/mnt/locust/locustfile.py","--master","-H","http://master:8089"]
ENTRYPOINT ["-f","/mnt/locust/locustfile.py","--worker","--master-host","master"]