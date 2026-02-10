import os
from constants import USER_PATH

class User:

    def __init__(self):
        self.username = None
        self.password = None
    
    def set_user_name(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password
    
    def create_user(self):

        if self.username and self.password:

            os.makedirs("database", exist_ok=True)

            # Create new User
            with open(USER_PATH, "a") as file:
                file.write(f"{self.username},{self.password}\n")
