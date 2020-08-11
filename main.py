import requests
import getpass
import sys

print("Welcome to ZeroGravity CLI")
#Greeter
def main():
    print("1.Login")
    print("2.Exit")
    ch1 = int(input(">> "))
    if ch1 == 1:
        login()
    elif ch1 == 2:
        sys.exit(0)
    else:
        print("Wrong Input")
        main()
        
# Login function        
def login():
    print("Please login")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    parameters = {"username":username , "password":password}
    response = requests.post("https://api.zerogravity.cc/v1/app/login",  data = parameters)
    data1 = response.json()
    print(data1)
    if data1["status"]  :
        global token
        token = data1["token"]
        print(token)
        fname = data1["fname"]
        print("Hi , "+fname)
        loggedin()
    else :
        print("Wrong login credentials")
        login()
#When logged in
def loggedin():
    print("1.App remote configuration")
    print("2.Change Password")
    print("3.Update mobile number")
    print("4.Logout")
    ch = int(input(">> "))
    if ch == 1:
        print("*******Work in progress*******")
        loggedin()
    elif ch == 2:
        changePass()
    elif ch == 3:
        upmn()
    elif ch == 4:
        logout()
    else:
        print("Wrong Input")
        loggedin()

#Change password        
def changePass():
    pass1 = getpass.getpass("Enter the current password: ")
    if pass1 == password:
        npass1 = getpass.getpass("Enter the new password: ")
        npass2 = getpass.getpass("Confirm the new password: ")
        if npass1 == npass2:
            cp = {"token":token,"currentPassword":password,"newPassword1":npass1,"newPassword2":npass2}
            r1 = requests.post("https://api.zerogravity.cc/v1/user/changePassword", data = cp)
            res1 = r1.json
            print("Password changes successfully")
            loggedin()
        else:
            print("Passwords don't match")
            loggedin()
    else:
        print("Incorrect password")
        loggedin()

#Update mobilenumber
def upmn():
    mob = int(input("Enter new mobile number: "))
    mob1 = {"token":token,"mobileNumber":mob}
    r2 = requests.post("https://api.zerogravity.cc/v1/user/updateMobileNumber",data = mob1)
    res2 = r2.json()
    print("Number updated successfully")
    loggedin()

#LogOut
def logout():
    tok = {"token":token}
    r3 = requests.post("https://api.zerogravity.cc/v1/user/logout",data = tok)
    res3 = r3.json()
    print(res3)
    main()

main()
