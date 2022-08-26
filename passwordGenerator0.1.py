from curses.ascii import isdigit
from re import X
import secrets, string, msvcrt

"""
TODO:
upperMin
lowerMin
digitMin
charcMin
"""
password = ""

def formulize(): 
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.punctuation)
    password += secrets.choice(string.digits)

while 0 < 1:
    print("Type length of password (0-9) ")
    print(60 * '-')
    try: 
        session_id = int(msvcrt.getch().decode('ASCII'))

        if isinstance(session_id, int) == True:
            #formulize(session_id)
            print(password)
            break
    
        elif session_id :
            print("Input not from 0-9. Try again")

    except:
        print('You are stupid. Use a number')
        



print(string.digits)