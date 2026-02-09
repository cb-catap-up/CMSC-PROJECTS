from constants import DESCRIPTION, START_SCREEN
from User.UserDataFetcher import UserDataFetcher
from Helpers.Helpers import Helpers

class Login:

    def showStartScreen():
        print(f"{START_SCREEN} \n")

        print(f"{DESCRIPTION} \n")

    def loginUser():
        Helpers.clearConsole()

        fetcher = UserDataFetcher()

        username = str(input("\nEnter Username: "))

        password = str(input("\nEnter Password: "))


        return fetcher.verify(username=username, password=password)
