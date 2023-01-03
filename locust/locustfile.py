import time
from locust import HttpUser, task, between, events
# const: 等待固定時間
# between: 等待在範圍內的隨機時間

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task(2)
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            if response.text != "Success":
                response.failure("Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")

    # @task(1)
    # def api(self):
    #     self.client.get("/api")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")
