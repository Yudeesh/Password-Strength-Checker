import re

def check_password(password):
    strength = "Weak"

    if len(password) >= 8:
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            if re.search("[0-9]", password):
                if re.search("[@#$%^&*]", password):
                    strength = "Strong"
                else:
                    strength = "Medium"

    return strength

password = input("Enter your password: ")
result = check_password(password)

print("Password Strength:", result)