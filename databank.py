import sqlite3
from operator import truediv

conn = sqlite3.connect(f"data/userscorelist.db")
cursor = conn.cursor()

def deinitialisedatabank():
    conn.close()

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


def save_userdata(userlist, userscores, user):
    entrylist = []
    for entry in userlist:
        entrylist.append(entry[1])
    if user in entrylist:
        cursor.execute(
            f"UPDATE users SET score = {userscores[user]} WHERE name = '{user}'"
        )
    else:
        newID = lowestID(userlist)
        cursor.execute(
            f"INSERT INTO users VALUES ({newID}, '{user}', {userscores[user]})"
        )
    conn.commit()


def get_userscores(userlist):
    userscores = {}
    for user in userlist:
        userscores.update({user[1]: user[2]})
    return userscores


def check_user_exist(userscores, user):
    r = f"{user}".lower()  # used to check if str input user exists in userlist
    if r in userscores:  # output is bool true or false
        return True
    else:
        return False


# print(lowestID(get_userlist()))
# userlist = get_userlist()
# userscores = get_userscores(get_userlist())
# userscores.update({"tom":2})
# save_userdata(userlist, userscores, "tom")
# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
#
#
# conn.close()  # gotta run conn.close() at the end atm
