from User.User import User

class Registration:

    def register_new_user():

        username = str(input("\nEnter Username: "))

        password = str(input("\nEnter Password: "))

        try: 
            new_user = User()
            new_user.set_user_name(username=username)
            new_user.set_password(password=password)
            new_user.create_user()

        except:
            print('An error has occured when creating user')
