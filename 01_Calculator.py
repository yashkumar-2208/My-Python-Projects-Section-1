print('A Calculator')

print("This calculator can perform calculations like: '+', '-', '*', '/', '//, '%', '**'" )
class calculator():
    def my_calculator():
        try:
            while True: 
                a = int(input("Enter the first numbers here for calculation: "))
                b = int(input("Enter the second seconds here for calculation: "))

                choices = ['+', '-', '*', '/', '//']
                user_choices = input("Enter your choice: ")
                if '+' in user_choices: 
                    print(f"The sum is: {a+b}")
                elif '-' in user_choices:
                    print(f"The difference is: {a-b}")
                elif '*' in user_choices:
                    print(f"The multiplication is: {a*b}")
                elif '/' in user_choices:
                    print(f"The division is: {a/b}")
                elif '//' in user_choices:
                    print(f"The floor division is: {a//b}")
                elif '%' in user_choices:
                    print(f"The modulus is: {a%b}")
                elif '**' in user_choices:
                    print(f"The power is: {a**b}")
                else:
                    print("Invalid input!")
                print("Operation executed successfully!")
        except Exception as e:
            print(f"Error: {e}")
            



calculator.my_calculator()