#this will be the data manager accessing and editing /data/Usercorelist.txt
#and translate their text into usable data for all other programs as well as be responsible for rewriting the data
#data:desc
#/data/Userscorelist.txt - Contains the users and their score in the format: "Username;Score"


# class Active_User:                                                                                                      #creating an active user class for maybe easier temp access
#     def __init__(self, name, progress):
#         self.name = name
#         self.__progress = progress
#
#     def get_progress(self):
#         return self.__progress



def get_userscores():                                                                                                   #get_userscores() reads out the Userscorelist.txt in data/ and provides the dictonary of users to the program as the variable Userscores
    Userscores = {}
    with open('data/Userscorelist.txt', 'rt') as f:
        for line in f:
            (key, val) = line.lower().strip().split(";")                                                                #Userscorelist.txt is supposed to be set as Username;Score per line for each user thus needs to be red as this and inserted into the dict with the dividing factor between strgs being ;
            try:                                                                                                        #in case of misakes in the user score resets score for security
                Userscores[key] = int(val)                                                                              #basically it deletes the progress but saves the user (maybe later usable for "New game option"
            except ValueError:
                Userscores[key] = 0
                print(f"No legal userscore found for {line.split(";")[0]}, set to 0")                                   #gotta check there is no ; in the username
        return Userscores                                                                                               #returns dictionary Userscores for further use ## dont forget to save it as a var



def check_user_exist(Userscores, user):                                                                                  #used to check if str input user exists in Userlist
    if user.lower() in Userscores:                                                                                      #output is bool true or false
        return True
    else:
        return False



def save_userdata(Userscores):                                                                                          #used to save the Userscores back in data/Userscorelist.txt
    with open('data/Userscorelist.txt', 'wt') as f:                                                                     #if it dosnt exist, a new one will be created in that folder
        for x in Userscores:
            f.write(f"{x.lower()};{Userscores[x]}\n")



def get_userprogress(Userscores, user):                                                                                 #used to return score of name from userscores
        return Userscores[user.lower()]



# Userscores = get_userscores()                         ##kontrollblock
# print(Userscores)
# x = input("Check if user exists")
# print(check_user_exist(Userscores,x))
# y = input("Check if this user exists as well")
# print(check_user_exist(Userscores,y))
# b = get_userprogress(Userscores, x)
# print(b)
