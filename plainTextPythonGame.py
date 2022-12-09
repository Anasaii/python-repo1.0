#semi finished. Choices need a bit of tweaking and variety

import random
import sys
import time
#from colored import fg
import msvcrt

def slowprint(s, speed=0.03):
     for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * speed)


# Start the game by introducing the situation and giving the player their first choice
slowprint("You wake up dazed and confused. You are on a plane that is falling from the sky. You do not know what is happening or why you are here. You see unconscious guards scattered around the cabin.")
slowprint("What do you do?")
slowprint("1. Try to take control of the plane")
slowprint("2. Search the unconscious guards for clues")
slowprint("3. Try to open the cabin door and jump out")

# Get the player's choice and decide which route to take
slowprint("Enter the number of your choice: \n")
session_id = (msvcrt.getch().decode('ASCII'))
if session_id == "1":
    # The player tries to take control of the plane
    slowprint("You try to take control of the plane, but you are not a trained pilot. You are unable to do anything and the plane continues to fall.")
    slowprint("What do you do now?")
    slowprint("1. Try to find a parachute and jump out of the plane")
    slowprint("2. Try to find something to defend yourself with in case the guards wake up")
    
    # Get the player's choice and decide which subroute to take
    slowprint("Enter the number of your choice: \n")
    session_id = (msvcrt.getch().decode('ASCII'))
    if session_id == "1":
        # The player tries to find a parachute and jump out of the plane
        slowprint("You search the cabin for a parachute and find one. You quickly put it on and prepare to jump out of the plane.")
        slowprint("As you are about to open the cabin door, the guards wake up and see what you are doing. They try to stop you, but you manage to open the door and jump out of the plane.")
        slowprint("You pull the parachute cord and glide safely to the ground. Congratulations, you have survived!")
    elif session_id == "2":
        # The player tries to find something to defend themselves with
        slowprint("You search the cabin for something to defend yourself with, but you are unable to find anything. The guards wake up and overpower you. They kill you and the plane continues to fall.")
        slowprint("You have died. Game over.")
    else:
        # The player entered an invalid choice
        slowprint("Invalid choice. You must choose 1 or 2.")
        slowprint("You are unable to do anything and the plane falls. You have died. Game over.")
elif session_id == "2":
# The player searches the unconscious guards for clues
    slowprint("You search the unconscious guards for clues, but you are unable to find anything. You are unable to do anything and the plane continues to fall.")
    slowprint("What do you do now?")
    slowprint("1. Try to find a parachute and jump out of the plane")
    slowprint("2. Try to find something to defend yourself with in case the guards wake up")
    # Get the player's choice and decide which subroute to take
    slowprint("Enter the number of your choice: \n")
    session_id = (msvcrt.getch().decode('ASCII'))
    if session_id == "1":
        # The player tries to find a parachute and jump out of the plane
        slowprint("You search the cabin for a parachute and find one. You quickly put it on and prepare to jump out of the plane.")
        slowprint("As you are about to open the cabin door, the guards wake up and see what you are doing. They try to stop you, but you manage to open the door and jump out of the plane.")
        slowprint("You pull the parachute cord and glide safely to the ground. Congratulations, you have survived!")
    elif session_id == "2":
        # The player tries to find something to defend themselves with
        slowprint("You search the cabin for something to defend yourself with, but you are unable to find anything. The guards wake up and overpower you. They kill you and the plane continues to fall.")
        slowprint("You have died. Game over.")
    else:
        # The player entered an invalid choice
        slowprint("Invalid choice. You must choose 1 or 2.")
        slowprint("You are unable to do anything and the plane continues to fall. You have died. Game over.")
elif session_id == "3":
    # The player tries to open the cabin door and jump out
    slowprint("You try to open the cabin door, but it is locked. You are unable to do anything and the plane continues to fall.")
    slowprint("What do you do now?")
    slowprint("1. Try to find a way to unlock the cabin door")
    slowprint("2. Try to find something to break the cabin door open")
    # Get the player's choice and decide which subroute to take
    slowprint("Enter the number of your choice:\n")
    session_id = (msvcrt.getch().decode('ASCII'))
    if session_id == "1":
        # The player tries to find a way to unlock the cabin door
        slowprint("You search the cabin for a way to unlock the cabin door, but you are unable to find anything. You are unable to do anything and the plane continues to fall.")
        slowprint("You have died. Game over.")
    elif session_id == "2":
        # The player tries to find something to break the cabin door open
        slowprint("You search the cabin for something to break the cabin door open, but you are unable to find anything. You are unable to do anything and the plane continues to fall.")
        slowprint("You have died. Game over.")
    else:
        # The player entered an invalid choice
        slowprint("Invalid choice. You must choose 1 or 2.")
        slowprint("You are unable to do anything and the plane continues to fall. You have died. Game over.")


