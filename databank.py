import sqlite3
from operator import truediv

conn = sqlite3.connect("data/Userscorelist.db")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, score INTEGER)")
# cursor.execute("INSERT INTO users VALUES (1, 'tom', 1)")
# cursor.execute("INSERT INTO users VALUES (2, 'max', 3)")
# cursor.execute("INSERT INTO users VALUES (3, 'felix', 0)")
# cursor.execute("INSERT INTO users VALUES (4, 'jessica', 0)")
# cursor.execute("INSERT INTO users VALUES (5, 'jaden', 0)")
# cursor.execute("DELETE FROM users WHERE id = 1")
# cursor.execute("DELETE FROM users WHERE id = 2")
# cursor.execute("DELETE FROM users WHERE id = 3")
# cursor.execute("DELETE FROM users WHERE id = 4")
# cursor.execute("DELETE FROM users WHERE id = 5")
# conn.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())


def get_userlist():
    cursor.execute("SELECT * FROM users")
    userlist = cursor.fetchall()
    return userlist


def lowestID(userlist):
    ID = 1
    IDlist = []
    for user in userlist:
        IDlist.append(user[0])
    while ID in IDlist:
        ID += 1
    return ID


# def save_user(userlist, )

def get_userscores(userlist):
    Userscores = {}
    for user in userlist:
        Userscores.update({user[1]: user[2]})
    return Userscores

def check_user_exist(Userscores, user):
    r = f"{user}".lower()  # used to check if str input user exists in Userlist
    if r in Userscores:  # output is bool true or false
        return True
    else:
        return False


# print(lowestID(get_userlist()))


conn.close()  # gotta run conn.close() at the end atm
