counter = 0
uid = input("Enter username: ")
pwd = input("Enter password: ")
def login():
    if(uid=="ADMIN" and pwd =="01234"):
        print("Login Successful")
        return
    else:
        print("The username or password is incorrect")
login()
