from User.User import User
from constants import USER_PATH

class UserDataFetcher(User):

    def verify(self, username: str, password: str):

        username_and_password_map = {}

        with open(USER_PATH, "r") as file:

            for line in file:

                saved_user_name, saved_password = line.strip().split(",")

                username_and_password_map[saved_user_name] = saved_password
        
        if not self._isUserPresent(username):

            print('User does not exist')

            return False
        
        if not username_and_password_map[username] == password:

            print('Wrong password')

            return False

        return True


    def _isUserPresent(self, username: str):
        try:
            with open(USER_PATH, "r") as file:
                for line in file:
                    saved_username, _ = line.strip().split(",")
                    if saved_username == username:
                        return True

        except FileNotFoundError:
            return False
        
        return False
