import random

chars="abcdefghijklmnoprstuyvzABCDEFGHIJKLMNOPRSTUYVZ1234567890!-?*&"

while 1:
    password_len= int(input("Pas length?"))
    password_count = int(input("How many?"))
    for x in range (0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print(password)