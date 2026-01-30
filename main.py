#this is the main user interface, from here we ll let the user login, access the rooms, and save their scores
#it ll require the functions of data.py, logic.py, and rooms.py to function

from data import *
from logic import *

def loginmenue():                                                                                                        #first test if user exists and loading of Userscorelist
    Input = input("Welcome please enter your Name")
    User = Input.lower()
    Userscores = get_userscores()
    Checkexist = bool(check_user_exist(Userscores, User))
    if Checkexist == False:
        print(f"\033[0;31m{User}\033[0m not found")
        newtry = input("Would you like to create a new profile? y/n")
        match newtry.lower():
            case "y":
                Userscores.update({User: 0})
                print(f"New User \033[0;34m{User}\033[0m created")
                mainmenue(User,Userscores)
            case _:
                print("returning to login")
                loginmenue()
    else:
        print(f"User \033[0;34m{User}\033[0m found")
        mainmenue(User,Userscores)



def mainmenue(User,Userscores):
    print(f"Greetings {User[0].upper()}{User[1:]} you are at room {Userscores[User]}")
    print(f"\n 1 --- Start  ---\n 2 --- Save   ---\n 3 --- Logout ---\n 4 --- Exit   ---\n")
    x = input("What would you like to do? ")
    match x:
        case "1":
            result = play_game(User, Userscores)

            if result == "exit":
                print("Returned to main menu.")

            if result == "victory":
                print("\n🎉 Congratulations, you completed the game!")

            mainmenue(User, Userscores)
        case "2":
            save_userdata(Userscores)
            mainmenue(User,Userscores)
        case "3":
            print("Logged out")
            loginmenue()
        case "4":
            print("Exiting, have a nice Day~")
        case _:
            print("Not a valid input, try again")
            mainmenue(User,Userscores)


loginmenue()