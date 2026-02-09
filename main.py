import datetime
from abc import ABC, abstractmethod

# =====================
# LOGGER
# =====================

class Logger:
    def log(self, msg):
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{t}] {msg}")

logger = Logger()

# =====================
# USER (inheritance)
# =====================

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass


class Admin(User):
    def role(self):
        return "admin"


class SimpleUser(User):
    def role(self):
        return "user"

# =====================
# PASSWORD MODEL
# =====================

class Account:
    def __init__(self, site, login, password):
        self.site = site
        self.login = login
        self.password = password

    def __str__(self):
        return f"{self.site} | {self.login} | {self.password}"

# =====================
# MANAGER
# =====================

class PasswordManager:
    def __init__(self):
        self.accounts = []

    def add(self, site, login, password):
        acc = Account(site, login, password)
        self.accounts.append(acc)
        logger.log("Qo‘shildi")

    def show(self):
        if not self.accounts:
            print("Bo‘sh")
            return
        for i, a in enumerate(self.accounts, 1):
            print(i, a)

    def delete(self, index):
        try:
            del self.accounts[index]
            logger.log("O‘chirildi")
        except:
            print("Xato index")

    def save(self):
        with open("data.txt", "w") as f:
            for a in self.accounts:
                f.write(f"{a.site}|{a.login}|{a.password}\n")
        logger.log("Saqlandi")

    def load(self):
        try:
            with open("data.txt") as f:
                for line in f:
                    site, login, password = line.strip().split("|")
                    self.accounts.append(Account(site, login, password))
        except:
            pass

# =====================
# MAIN
# =====================

def main():
    manager = PasswordManager()
    manager.load()

    user = Admin("Ali")
    logger.log(f"Login: {user.name} ({user.role()})")

    while True:
        print("\n1.Add 2.Show 3.Delete 4.Save 0.Exit")
        c = input(">>> ")

        if c == "1":
            s = input("Site: ")
            l = input("Login: ")
            p = input("Password: ")
            manager.add(s, l, p)

        elif c == "2":
            manager.show()

        elif c == "3":
            i = int(input("Index: ")) - 1
            manager.delete(i)

        elif c == "4":
            manager.save()

        elif c == "0":
            manager.save()
            break


if __name__ == "__main__":
    main()
