from locust import HttpUser, TaskSet, task, between

class LoginTest(TaskSet):
    @task(1)
    def login(self):
        payload = {
            "email": "john.doe@gmail.com", 
            "password": "SecurePassword_123"
        }
        with self.client.post("http://localhost:8000/login/", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()  
            else:
                response.failure(f"Failed with status {response.status_code}")  

class WebsiteUser(HttpUser):
    tasks = [LoginTest]
    wait_time = between(1, 20)  # Затримка між запитами 
