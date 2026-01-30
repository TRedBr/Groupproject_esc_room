#this is the main user interface, from here we ll let the user login, access the rooms, and save their scores
#it ll require the functions of data.py, logic.py, and rooms.py to function

from data import *
from databank import *


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



def mainmenue(user,userscores,userlist):
    print(f"Greetings {user[0].upper()}{user[1:]} you are at room {userscores[user]}")                                  #Main menue greets user and provides their data from userdata for further processes
    print(f"\n 1 --- Start  ---\n 2 --- Save   ---\n 3 --- Logout ---\n 4 --- Exit   ---\n")
    x = input("What would you like to do? ")
    match x:
        #case "1":                                                                                                      #Link to logic, and the game, can provide userscores dict, user and userscore as ressources to game logic
        case "2":
            save_userdata(userlist,userscores,user)#Link to data, provides userscores Dict for writing in .txt            save_userdata(userscores)
            mainmenue(user,userscores,userlist)
        case "3":                                                                                                       #returns to login with no data saved, might change it to ask if user wants to save before exiting
            print("Logged out")
            loginmenue()
        case "4":                                                                                                       #ends the program dosnt save the data, might change it to ask if user wants to save before exiting
            print("Exiting, have a nice Day~")
            deinitialisedatabank()
        case _:                                                                                                         #reruns the function
            print("Not a valid input, try again")
            mainmenue(user,userscores,userlist)


loginmenue()