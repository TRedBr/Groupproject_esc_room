#this is the main user interface, from here we ll let the user login, access the rooms, and save their scores
#it ll require the functions of data.py, logic.py, and rooms.py to function

from data import *
from logic import *

def loginmenue():                                                                                                       #first test if user exists and loading of Userscorelist
    Input = input("Welcome please enter your Name")                                                                     #than logs in or registers the user to proceed to the main menu
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
    print(f"Greetings {User[0].upper()}{User[1:]} you are at room {Userscores[User]}")                                  #Main menue greets user and provides their data from Userdata for further processes
    print(f"\n 1 --- Start  ---\n 2 --- Save   ---\n 3 --- Logout ---\n 4 --- Exit   ---\n")
    x = input("What would you like to do? ")
    match x:
        #case "1":                                                                                                      #Link to logic, and the game, can provide Userscores dict, User and Userscore as ressources to game logic
        case "2":                                                                                                       #Link to data, provides Userscores Dict for writing in .txt            save_userdata(Userscores)
            mainmenue(User,Userscores)
        case "3":                                                                                                       #returns to login with no data saved, might change it to ask if user wants to save before exiting
            print("Logged out")
            loginmenue()
        case "4":                                                                                                       #ends the program dosnt save the data, might change it to ask if user wants to save before exiting
            print("Exiting, have a nice Day~")
        case _:                                                                                                         #reruns the function
            print("Not a valid input, try again")
            mainmenue(User,Userscores)


loginmenue()