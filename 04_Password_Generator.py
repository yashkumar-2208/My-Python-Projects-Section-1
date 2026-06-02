
# 1. string.ascii_lowercase
# - The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
# 2. string.ascii_uppercase
# - The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
# 3. string.digits
# - The string '0123456789'.
# 4. string.hexdigits
# - The string '0123456789abcdefABCDEF'.
# 5. string.octdigits
# - The string '01234567'.
# 6. string.punctuation
# - String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.



import random
import string

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation

all_combine = a+b+c+d


while True:
    user = input("Enter here: ").capitalize()

    if user in [
        "generate password",
        "generate pass",
        "generate password for me",
        "generate Password",
        "Generate password",
        "generate Password",
        "generate pass",
        "Generate pass",
        "generate Pass"
    ]:

        password = ""
        for i in range(12):
            password += random.choice(all_combine)
        print(f"Your generated password is: {password}")
            
    else:
        print("Sorry")