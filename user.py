import sqlite3
from encription import encrypt, decrypt


class User:
    def __init__(self):
        self.username = ""
        self.mail = ""
        self.pwd = ""

    def save(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        params = (self.username, self.mail, encrypt(self.pwd))
        c.execute("INSERT INTO user VALUES (?, ?, ?)", params)
        conn.commit()
        conn.close()

    def load(self, username):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        params = (username,)
        c.execute("SELECT * FROM user WHERE username=?", params)
        data = c.fetchone()
        conn.close()
        self.username = data[0]
        self.mail = data[1]
        self.pwd = decrypt(data[2])

    def create(self):
        self.username = input("Username: ")
        self.mail = input("Mail:     ")
        self.pwd = input("Password: ")
        self.save()

    def delete(self):
        username = input("Welcher Benutzer soll gelöscht werden? ")
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        params = (username,)
        c.execute("DELETE FROM user WHERE username=?", params)
        conn.commit()
        conn.close()


class CurrentUser(User):
    def __init__(self, username):
        super().__init__()
        self.load(username)
