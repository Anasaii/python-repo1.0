from pickle import NONE
import random
from turtle import done
import pyperclip
from curses.ascii import isdigit
from re import X
import secrets
import string
import msvcrt
import time
import re


"""
TODO:
upperMin = -u
lowerMin = -l
digitMin = -d
charcMin = -c
passLength
all
last used (requires json)
upcoming
"""

def passlen():
    password_length = input("Enter password length: ")
    return password_length

def upperMin():
    uppercase_minimum = input("Enter upppercase minimum: ")
    return uppercase_minimum

def lowerMin():
    lowercase_minimum = input("Enter lowercase minimum: ")
    return lowercase_minimum

def digitMin():
    digit_minimum = input("Enter digit minimum: ")
    return digit_minimum

def charcMin():
    special_minimumum = input("Enter special chacter minimum")
    return special_minimumum

def useALL():
    x = "you returned all you fucking dimwit, goodjob"
    return x

def invalidFlag():
    raise Exception("Invalid flag")

def choose_flag(flag):
    options = {
        "-all" : useALL,
        "-u" : upperMin,
        "-l" : lowerMin,
        "-d" : digitMin,
        "-c" : charcMin
    }

    value_got = options.get(flag, invalidFlag)
    return value_got()




def custom_formulize(tupledSearchedFlags):
    value = choose_flag(tupledSearchedFlags)
    return value

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

    #advanced settings
    if session_id == "\r":
        print("                  Entering advanced settings... \n")
        time.sleep(.5)
        print("-Flags:\n [     useAll   = -all] [   lastUsed   =  -lu] \n [ uppercaseMin =   -u] [ lowercaseMin =   -l] \n [   digitsMin  =   -d] [  specialMin  =   -c] \n [  passLength  =   -p]")

    
        allowedFlags = ('-p', '-u', '-l', '-d', '-c', '-all', '-lu')
        flags = input("\n")
        searchedFlags = re.split("\s", flags)
        passFlag = any(item in searchedFlags for item in allowedFlags)
    

        if passFlag == True:
            done = choose_flag(searchedFlags[0])
            print(done)

        break

        #commands not followed
    elif isinstance(session_id, str) == True:
        print('                 You are stupid. Use a number.')

        #digit given
    elif isinstance((session_id), int) == True:
        session_id = int(session_id)
        finalPassword = (default_formulize(session_id))
        print("\n", finalPassword)
        #pyperclip.copy(finalPassword)
        break

        #catch unknown characters
    else:
        print("an error has occured")
