from locust import HttpUser, SequentialTaskSet, task, constant
import re

class tasks(SequentialTaskSet):
    # @task(2)
    @task
    def hi_nginx(self):
        self.client.get("")
    # @task(1)
    # def api(self):
    #     self.client.get("/api")


class LoadTest(HttpUser):
    # host = nginx
    host = https://www.youtube.com/
    wait_time = constant(1)
    tasks = [tasks]