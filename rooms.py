#Manages the rooms, and their intern logic for returning false and true from the answers
#creates functions per room, and provides the room index numbers

class Room:
    def __init__(self, name, task, answer):
        self.name = name
        self.task = task
        self.__answer = answer

    def get_antwort(self):
        return self.__antwort

    def room_execute(self):
        print(f"\nHello! Welcome at the {self.name}.")
        print(f"Task: {self.task}")
        enter =  input("Please enter your answer: ")

        if enter == self.__answer:
            return True
        else:
            return False

r1 = Room("Math-Door", "What is (5+10)*2?", "30")