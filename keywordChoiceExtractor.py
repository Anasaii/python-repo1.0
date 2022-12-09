import random
import sys
import time
from colored import fg
import time
import msvcrt



def slowprint(s, speed=0.01):
     for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * speed)




def checkStr(dialogue, input_list):

    flag = False

    while flag == False:
        slowprint(dialogue)
        test_string = input("\n::")
        test_list = test_string.split(" ")
        n = [
    "don't",
    "not",
    "never",
    "neither",
    "neither",
    "nor",
    "barely",
    "hardly",
    "scarcely",
    "seldom",
    "rarely",
    "won't"
  ]
        for i in test_list:
            for j in n:
                if i == j:
                    print("Ambiguity detected")
                    print("\n")
                    return j

        for i in test_list:
            for j in input_list:
                if i == j:
                    flag = True
                    return j


        if flag == False:

            print("Invalid Input: " + test_string)

part1 = checkStr("I am so damn cool", ["Yes", "ok"])
