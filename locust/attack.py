from locust import HttpUser, SequentialTaskSet, task, constant
import re

class tasks(SequentialTaskSet):
    @task(2)
    def hi_nginx(self):
        with self.client.get("/", catch_response=True) as response:
            if response.text != "Success":
                response.failure("Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")
    @task(1)
    def api(self):
        self.client.get("/api")


class LoadTest(HttpUser):
    host = nginx
    wait_time = constant(1)
    tasks = [tasks]