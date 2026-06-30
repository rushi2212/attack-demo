from locust import HttpUser, task, between, constant
import random


class DDoSUser(HttpUser):
    # Minimal wait time to simulate aggressive attack
    wait_time = constant(0.1)  # 100ms between requests

    @task(90)
    def attack_root(self):
        """Hammer the root endpoint"""
        self.client.get("/")

    @task(10)
    def check_health(self):
        """Occasionally check health endpoint"""
        self.client.get("/health")
