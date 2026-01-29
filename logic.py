# this will contain the logic of game tracking the players progress(score) responsible for User interaction if answers are true or false, and processes
# if player advances a room(score) or repeats it. Checks if all rooms are cleared.
##requires data.py and rooms.py
from rooms import r1, r2, r3
from data import get_userscores, check_user_exist, get_userprogress, save_userdata


class Game:                 #since the rooms are already classes you might consider making them an inner class
    def __init__(self):     ##alternatively it is questionable if you want to run the game as a class, as it would require initialisation of a game object from main.py
        self.rooms = [r1, r2, r3]
        self.current_room_index = 0
        self.username = ""
        self.userscores = get_userscores()

    def new_game(self):
        self.username = input("Please enter your username: ").strip()

        if not check_user_exist(self.userscores, self.username):
            self.userscores[self.username] = 0 #always resets to 0
        print(f"Welcome {self.username}, let's start the game!")

        while self.current_room_index < len(self.rooms):
            current_room = self.rooms[self.current_room_index]

            while not current_room.room_execute():
                pass

            self.current_room_index += 1
            save_userdata(self.userscores)

        print("Congratulations! You've completed the Game.")

        self.userscores[self.username] = self.current_room_index
        save_userdata(self.userscores)

    def load_game(self):
        if check_user_exist(self.userscores, self.username):
            user_score = get_userprogress(self.userscores, self.username)
            self.current_room_index = user_score
            print(f"Welcome back {self.username}, resuming from room {self.current_room_index} + 1.")

        while self.current_room_index < len(self.rooms):
            current_room = self.rooms[self.current_room_index]

            while not current_room.room_execute():
                pass

            self.current_room_index += 1
            save_userdata(self.userscores)

        print("Congratulations! You've completed the Game.")


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