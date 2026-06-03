import random
import string 

class OTP_Generator():

    def otp():

        try:

            a = string.digits

            print("- To generate 4 digits otp press '1'")
            print("- To generate 6 digits otp press '2'")

            user_input = int(input("Enter here: "))

            if user_input == 1:

                otp = ""
                for i in range(4):
                    otp += random.choice(a)
                print(f"Your generated otp is: {otp}")

            elif user_input == 2:

                otp = ""
                for i in range(6):
                    otp += random.choice(a)
                print(f"Your generated otp is: {otp}")


            else:
                print("Error!")            

        except Exception as e:
            print(f"Error {e}")


OTP_Generator.otp()


