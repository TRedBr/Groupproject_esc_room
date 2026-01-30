#this will be the data manager accessing and editing /data/usercorelist.txt
#and translate their text into usable data for all other programs as well as be responsible for rewriting the data
#data:desc
#/data/userscorelist.txt - Contains the users and their score in the format: "username;Score"


# class Active_user:                                                                                                      #creating an active user class for maybe easier temp access
#     def __init__(self, name, progress):
#         self.name = name
#         self.__progress = progress
#
#     def get_progress(self):
#         return self.__progress



# def get_userscores(userlist):                                                                                                   #get_userscores(userlist) reads out the userscorelist.txt in data/ and provides the dictonary of users to the program as the variable userscores
#     userscores = {}
#     with open('data/userscorelist.txt', 'rt') as f:
#         for line in f:
#             (key, val) = line.lower().strip().split(";")                                                                #userscorelist.txt is supposed to be set as username;Score per line for each user thus needs to be red as this and inserted into the dict with the dividing factor between strgs being ;
#             try:                                                                                                        #in case of misakes in the user score resets score for security
#                 userscores[key] = int(val)                                                                              #basically it deletes the progress but saves the user (maybe later usable for "New game option"
#             except ValueError:
#                 userscores[key] = 0
#                 print(f"No legal userscore found for {line.split(";")[0]}, set to 0")                                   #gotta check there is no ; in the username
#         return userscores                                                                                               #returns dictionary userscores for further use ## dont forget to save it as a var
# 
# 
# 
# def check_user_exist(userscores, user):
#     r = f"{user}".lower()#used to check if str input user exists in userlist
#     if r in userscores:                                                                                                 #output is bool true or false
#         return True
#     else:
#         return False
# 
# 
# 
# def save_userdata(userscores):                                                                                          #used to save the userscores back in data/userscorelist.txt
#     with open('data/userscorelist.txt', 'wt') as f:                                                                     #if it dosnt exist, a new one will be created in that folder
#         for x in userscores:
#             f.write(f"{x.lower()};{userscores[x]}\n")
# 
# 
# 
# def get_userprogress(userscores, user):                                                                                 #not tested                                                                          #used to return score of name from userscores
#         return userscores[user.lower()]



# userscores = get_userscores(userlist)                         ##kontrollblock
# print(userscores)
# x = input("Check if user exists")
# print(check_user_exist(userscores,x))
# y = input("Check if this user exists as well")
# print(check_user_exist(userscores,y))
# b = get_userprogress(userscores, x)
# print(b)