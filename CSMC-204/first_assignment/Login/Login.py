from constants import DESCRIPTION, START_SCREEN
from User.UserDataFetcher import UserDataFetcher
from Helpers.Helpers import Helpers

class Login:

    def show_start_screen():
        print(f"{START_SCREEN} \n")

        print(f"{DESCRIPTION} \n")

    def login_user():
        Helpers.clear_console()

        fetcher = UserDataFetcher()

        username = str(input("\nEnter Username: "))

        password = str(input("\nEnter Password: "))


        return fetcher.verify(username=username, password=password)
