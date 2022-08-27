from pickle import NONE
import random
import pyperclip
from curses.ascii import isdigit
from re import X
import secrets
import string
import msvcrt
import time
"""
TODO:
upperMin = -u
lowerMin = -l
digitMin = -d
charcMin = -c
"""


def default_formulize(a):
    password = []
    finalPassword = ""

    for x in range(a):
        password.append(secrets.choice([secrets.choice(string.ascii_letters), secrets.choice(
            string.punctuation), secrets.choice(string.digits)]))
        #print(password)

    random.shuffle(password)
    finalPassword = ''.join(map(str, password))
    return finalPassword


while 0 < 1:

    print("\n |",60 * '-',"|", "\n | Type length of password (0-9). Press enter for more options. | \n", "|",60 * '-',"|")


    # Getch user input
    session_id = (msvcrt.getch().decode('ASCII'))
    # Convert to int if digit
    if session_id in string.digits:
        session_id = int(session_id)
    # print(session_id)

    if session_id == "\r":
        print("Entering Complex settings...")
        time.sleep(.5)
        print("-Flags:\n [  passLength  = -p] \n [ uppercaseMin = -u] \n [ lowercaseMin = -l] \n [   digitsMin  = -d] \n [  specialMin  = -c]")
        flags = input("")
        break

    elif isinstance(session_id, str) == True:
        print("\n"), print(60 * '-'), print('You are stupid. Use a number')

    elif isinstance((session_id), int) == True:
        session_id = int(session_id)
        finalPassword = (default_formulize(session_id))
        print("\n", finalPassword)
        pyperclip.copy(finalPassword)
        break

    else:
        print("an error has occured")
