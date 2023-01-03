from locust import events
from locust.runners import MasterRunner, WorkerRunner

# Fired when the worker receives a message of type 'test_users'
def setup_test_users(environment, msg, **kwargs):
    for user in msg.data:
        print(f"User {user['name']} received")
    environment.runner.send_message('acknowledge_users', f"Thanks for the {len(msg.data)} users!")

# Fired when the master receives a message of type 'acknowledge_users'
def on_acknowledge(msg, **kwargs):
    print(msg.data)

@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    if not isinstance(environment.runner, MasterRunner):
        environment.runner.register_message('test_users', setup_test_users)
    if not isinstance(environment.runner, WorkerRunner):
        environment.runner.register_message('acknowledge_users', on_acknowledge)
    
@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    if not isinstance(environment.runner, MasterRunner):
        users = [
            {"name": "User1"},
            {"name": "User2"},
            {"name": "User3"},
        ]
        environment.runner.send_message('test_users', users)