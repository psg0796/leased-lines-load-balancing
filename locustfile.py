from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    # @task(1)
    # def index(self):
    #     self.client.get("/")

    @task(1)
    def search_a(self):
        self.client.get("/docs/react/getting-started")
    
    # @task(1)
    # def search_absolute(self):
    #     self.client.get("/3Percent/S02/480p/3.Percent.S02E01.480p.WEB.RMT.Farda.DL.mkv")

    # @task(1)
    # def search_deepLea(self):
    #     self.client.get("/Batman%3a%20The%20Animated%20Series/S03/1080p%20x265/Batman.The.Animated.Series.S03E01.Bane.1080p.BluRay.x265.HET.Farda.DL.mkv")

    # @task(1)
    # def search3(self):
    #     self.client.get("/wiki/QWERTY")

class WebsiteUser(HttpLocust):
    # host = 'http://youtube.com'
    # host = 'http://google.com'
    host = 'https://ant.design'
    
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
