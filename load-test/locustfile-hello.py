from locust import task, FastHttpUser

class HelloWorld(FastHttpUser):
    connection_timeout = 10.0
    network_timeout = 10.0

    @task
    def hell0(self):
        self.client.get("/hello")