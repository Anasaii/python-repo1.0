import random
import sys
import time
from colored import fg
import time
import msvcrt

blue = fg('blue')
red = fg('red')
normal = fg('orchid_2')
white = fg('white')
magenta = fg('magenta')
gold = fg("gold_1")

def slowprint(s, speed=0.01):
     for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * speed)



def Arc(maindoor, enemy, maincolor, enemycolor):
    slowprint(white + "You wake up as a " + maincolor + maindoor.rstrip(maindoor[-1]) + white)
    slowprint("You are enemies of the " + enemycolor + enemy + white)
    slowprint("In front of you stands a " + enemycolor + enemy.rstrip(enemy[-1]) + white)
    slowprint("You feel an overwhelming sense of malice emiting around this door")
    time.sleep(1)
    slowprint("\n")
    slowprint(white + "You look around and various " + maincolor + maindoor + white + " await your response")
    slowprint(magenta + "\"Complete the ritual.... and you become one of us.\"")
    slowprint(gold + "Do you kill the door?", 0.05)
    decision1(enemy, maincolor, enemycolor )


def decision1(enemy, maincolor, enemycolor):
    while 1 > 0:
        slowprint("Y or N")
        session_id = (msvcrt.getch().decode('ASCII'))
        print(session_id)
        if session_id == "y":
            slowprint(red + "You open yourself and hit the " + enemycolor + enemy.rstrip(enemy[-1]) + maincolor +" with your doornob.")
            slowprint("The crowd roars")
            break
        elif session_id == "n":
            slowprint("You don't know if your decision was the wisest, but you stop and ponder harder")
            slowprint("Should I really do this?")
            break
        else:
            slowprint("I have to really think about this")



def blueArc():
    slowprint(white + "You wake up as a " + blue + "BLUE DOOR.")
    slowprint("You are enemies of the " + red + "RED DOORS." + red)
    slowprint("In front of you stands a " + red + "RED DOOR." + red)

while 1 > 0:
    userDoor = input("Are you a " + red + "RED DOOR " + white + "or a " + blue + "BLUE DOOR?\n")

    if userDoor == "red":
        Arc("RED DOORS", "BLUE DOORS", red, blue)
        break
    elif userDoor == "blue":
        Arc("BLUE DOORS", "RED DOORS", blue, red)
        break
    else:
        print(white +"Invalid Option\n")



