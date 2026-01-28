#this is the main user interface, from here we ll let the user login, access the rooms, and save their scores
#it ll require the functions of data.py, logic.py, and rooms.py to function

from data import *

def loginmenue():                                                                                                        #first test if user exists and loading of Userscorelist
    User = input("Welcome please enter your Name")
    Userscores = get_userscores()
    Checkexist = check_user_exist(userscores, User)
    if Checkexist == False:
        print(f"\033[0;31m{User}\033[0m not found")
        newtry = input("Would you like to create a new profile? y/n")
        match newtry.lower():
            case "y":
                userscores.update({User.lower: 0})
                print(f"New User \033[0;34m{User}\033[0m created")
                mainmenue(User,Userscores)
            case _:
                print("returning to login")
                loginmenue()
    else:
        print(f"User \033[0;34m{User}\033[0m found")
        mainmenue(User,Userscores)



def mainmenue(User,Userscores):
    print(f"Greetings {User} you are at room {Userscores[User.lower]}")
    print(f"\n 1 --- Start ---\n 2 --- Save ---\n 3 --- Exit")
    x = input("What would you like to do?")
    match x:
        #case "1":
        case "2":
            save_userdata(Userscores)
            mainmenue(User,Userscores)
        case "3":
            print("Exiting back to login Menu")
            loginmenue()
        case _:
            print("Not a valid input, try again")
            mainmenue(User,Userscores)
