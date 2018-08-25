from user import User, CurrentUser
from encription import encrypt, decrypt
import sqlite3

defs = {"1": User().create,
        "2": User().modify,
        "3": User().delete}

def menu():
    print("1 | Nutzer erstellen \n"
          "2 | Nutzer bearbeiten \n"
          "3 | Nutzer löschen")
    c = input("Möglichkeit auswählen: ")
    defs[c]()


def login(count):
    username = input("Username: ")
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    params = (username,)
    try:
        c.execute("SELECT * FROM user WHERE username=?", params)
        user = c.fetchone()
        password = input("Passwort: ")
        if password == decrypt(user[2]):
            print("Login erfolgreich!")
            current = CurrentUser(username)
    except:
        count += 1
        print("Nutzer existiert nicht!")
        if count < 3:
            print("Noch", 3 - count, "Versuche!")
            login(count)
            exit()
    menu()


login(0)
