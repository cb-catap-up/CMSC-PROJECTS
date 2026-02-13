from constants import DESCRIPTION, START_SCREEN, LOGIN
from User.UserDataFetcher import UserDataFetcher
from Helpers.Helpers import Helpers

class Login:

    def show_start_screen():
        print(f"{START_SCREEN} \n")

        print(f"{DESCRIPTION} \n")

    def login_user():
        Helpers.clear_console()

        fetcher = UserDataFetcher()

        print(f"{LOGIN} \n")

        username = str(input("Enter Username: "))

        password = str(input("\nEnter Password: "))

        # return user name
        return fetcher.verify(username=username, password=password)
