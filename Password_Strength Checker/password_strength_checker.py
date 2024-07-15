import re


def is_strong_password(password):

    #for checking length of password(min 8 char)
    if len(password)<8:
        return False
    
    #for checking uppercase
    if not any (char.isupper() for char in password):
        return False
    
    #check for lowercase
    if not any(char.islower() for char in password):
        return False
    
    #for checking digits
    if not any(char.isdigit() for char in password):
        return False

    #for checking special characters
    if not any(char in "!@#$%^&*()_+" for char in password):
        return False
    return True

def main():
    password = input("Enter your password:")

    if is_strong_password(password):
        print("Strong password")
    else:
        print("Weak password")

if __name__=="__main__":
    main()