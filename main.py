from user import User, CurrentUser
from encription import encrypt, decrypt
import sqlite3

defs = {"1": User().create,
        "2": print,
        "3": User().delete}


def menu():
    print("1 | Nutzer erstellen \n"
          "2 | Nutzer bearbeiten \n"
          "3 | Nutzer löschen")
    c = input("Möglichkeit auswählen: ")
    defs[c]()


def login():
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
            menu()
    except:
        print("Nutzer existiert nicht!")


login()