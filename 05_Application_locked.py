#05: Application locker app

import time
import pwinput


class app_locker():

    def app_lock():

        try: 

            #password = pwinput.pwinput("Please set your password here: ",mark=".")
            #mark is used to change the symbol.

            password = pwinput.pwinput("Please set your password here: ")
            print("Password set successfully!")

            while True:

                user = pwinput.pwinput("Please enter your password here to unlock your application: ")

                if password == user:
                    print("Application unlocked successfully!")
                    break
                    

                elif user != password:
                    print("You have three attempts left!")

                user = pwinput.pwinput("Please enter your correct password here to unlock your application: ")

                if password == user:
                    print("Application unlocked successfully")
                    break

                elif user != password:
                    print("You have two attempts left!")


                user = pwinput.pwinput("Please enter your correct password here to unlock your application: ")

                if password == user:
                    print("Application unlocked successfully")
                    break


                elif user != password:
                    print("You have last attempt left!")

                user = pwinput.pwinput("Please enter your correct password here to unlock your application: ")

                if password == user:
                    print("Application unlocked successfully")
                    break

                elif user != password:
                    print("You had attempted all three attempts now you can re-enter your password after 5 seconds")
                    time.sleep(5)

        except Exception as e:
            (f"Error: {e}")

app_locker.app_lock()