#this is the main user interface, from here we ll let the user login, access the rooms, and save their scores
#it ll require the functions of data.py, logic.py, and rooms.py to function

from data import *
from databank import *
from logic import *


def loginmenue():#first test if user exists and loading of userscorelist
    Input = input("Welcome please enter your Name")                                                                     #than logs in or registers the user to proceed to the main menu
    user = Input.lower()
    userlist = get_userlist()
    userscores = get_userscores(userlist)
    Checkexist = bool(check_user_exist(userscores, user))
    if Checkexist == False:
        print(f"\033[0;31m{user}\033[0m not found")
        newtry = input("Would you like to create a new profile? y/n")
        match newtry.lower():
            case "y":
                userscores.update({user: 0})
                print(f"New user \033[0;34m{user}\033[0m created")
                mainmenue(user,userscores,userlist)
            case _:
                print("returning to login")
                loginmenue()
    else:
        print(f"user \033[0;34m{user}\033[0m found")
        mainmenue(user,userscores,userlist)



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
            deinitialisedatabank()
        case _:                                                                                                         #reruns the function
            print("Not a valid input, try again")
            mainmenue(user,userscores,userlist)


loginmenue()