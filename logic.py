# this will contain the logic of game tracking the players progress(score) responsible for User interaction if answers are true or false, and processes
# if player advances a room(score) or repeats it. Checks if all rooms are cleared.
##requires data.py and rooms.py
from rooms import r1, r2, r3
from data import get_userscores, check_user_exist, get_userprogress, save_userdata


class Game:
    def __init__(self):
        self.rooms = [r1, r2, r3]
        self.current_room_index = 0
        self.username = ""
        self.userscores = get_userscores()

    def new_game(self):
        self.username = input("Please enter your username: ").strip()

        if not check_user_exist(self.userscores, self.username):
            self.userscores[self.username] = 0
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
