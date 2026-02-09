from User.User import User

class Registration:

    def registerNewUser():

        username = str(input("\nEnter Username: "))

        password = str(input("\nEnter Password: "))

        try: 
            new_user = User()
            new_user.setUserName(username=username)
            new_user.setPassWord(password=password)
            new_user.createUser()

        except:
            print('An error has occured when creating user')
