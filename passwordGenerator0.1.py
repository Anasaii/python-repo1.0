import random
import pyperclip
from curses.ascii import isdigit
from re import X
import secrets, string, msvcrt

"""
TODO:
upperMin = -u
lowerMin = -l
digitMin = -d
charcMin = -c
"""


def formulize(a): 
    password = []
    finalPassword = ""

    for x in range(a):
        password.append(secrets.choice([secrets.choice(string.ascii_letters), secrets.choice(string.punctuation), secrets.choice(string.digits)]))
        print(password)

    random.shuffle(password)
    finalPassword = ''.join(map(str, password))
    return finalPassword

while 0 < 1:
    print("Type length of password (0-9) ")
    print(60 * '-')
    session_id = int(msvcrt.getch().decode('ASCII'))

    if isinstance(session_id, int) == True:
        finalPassword = (formulize(session_id))
        print(finalPassword)
        pyperclip.copy(finalPassword)
        break
        
    else: 
        print('You are stupid. Use a number')


    #except:
        print('You are stupid. Use a number')
        