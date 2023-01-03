import time
from locust import HttpUser, task, between, events
# const: 等待固定時間
# between: 等待在範圍內的隨機時間

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("")


    # @task(1)
    # def api(self):
    #     self.client.get("/api")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")
    
'''
def checker(environment):
    while not environment.runner.state in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
        time.sleep(1)
        if environment.runner.stats.total.fail_ratio > 0.2:
            logging.info(f"fail ratio was {environment.runner.stats.total.fail_ratio}, quitting")
            environment.process_exit_code = 2
            environment.runner.quit()
            return

@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    print("A new test is starting")
    if not isinstance(environment.runner, WorkerRunner):
        gevent.spawn(checker, environment)
'''