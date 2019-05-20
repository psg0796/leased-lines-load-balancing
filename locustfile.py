from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def search_a(self):
        self.client.get("/watch?v=yv5i0oTHubc&t=512s")
    
    @task(1)
    def search_absolute(self):
        self.client.get("/watch?v=n-RjGEWW3nk&t=50")

    # @task(1)
    # def search_deepLea(self):
    #     self.client.get("/wiki/Deep_learning")

    # @task(1)
    # def search3(self):
    #     self.client.get("/wiki/QWERTY")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000