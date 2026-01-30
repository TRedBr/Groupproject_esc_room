# Manages the rooms, and their intern logic for returning false and true from the answers
# creates functions per room, and provides the room index numbers

class Room:
    def __init__(self, name, task, answer):
        self.name = name
        self.task = task
        self.__answer = answer

    def get_answer(self):
        return self.__answer

    def room_execute(self):
        print(f"\nHello! Welcome at the {self.name}.")
        print(f"Task: {self.task}")
        user_input = input("Please enter your answer (or 'exit'): ").strip()

        if user_input == "exit":
            return "exit"

        if user_input == self.__answer:
            print("Correct answer.")
            return True
        else:
            print("Incorrect answer, try again.")
            return False


r1 = Room(
    "Math-Door",
    "What is (5+10)*2?",
    "30"
)
r2 = Room(
    "Number-Filter-Panel",
    "Enter all the even numbers from this list: [3,10,15,22,7]",
    "10 22"
)
r3 = Room(
    "Password-Terminal",
    "Enter the password. (Hint: python + 123)",
    "python123"
)

##---TRedBr---Comment
#rooms all work
#r3 missing a ) after the hint