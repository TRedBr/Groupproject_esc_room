# this will contain the logic of game tracking the players progress(score) responsible for user interaction if answers are true or false, and processes
# if player advances a room(score) or repeats it. Checks if all rooms are cleared.
##requires data.py and rooms.py
from rooms import r1, r2, r3

rooms = [r1, r2, r3]

def play_game(user, userscores):
    current_room_index = userscores[user]

    while current_room_index < len(rooms):
        current_room = rooms[current_room_index]

        while True:
            result = current_room.room_execute()

            if result == "exit":
                userscores[user] = current_room_index
                return "exit"

            if result is True:
                break

        current_room_index += 1
        userscores[user] = current_room_index

    return "victory"

def reset_game(user, userscores):
    putin = input("To reset press r: ")
    match putin.lower():
        case "r":
            print("Your progress was reset.")
            userscores[user] = 0
        case _:
            print("Returnin to menu.")

#controll block
# Thisgame = Game()
# Thisgame.new_game()


#---TRedBr---comment

#new_game Works

##Game wasn't supposed to autosave

##needs an option to exit out between rooms

##needs a function for manual saves

##it would be best to leave the .strip() in for data reasons

##how do you differenciate between .new_game() and .load_game(), also since loadgame has no intake
##it will run with the default ""

##add option on victory, to leave, (save and leave) or instantly repeat, similar question logic at the start, instead of
##automatically assuming maxed out players want to repeat

##main menu can feed user and userscores, playing it as a class complicates the functionality
