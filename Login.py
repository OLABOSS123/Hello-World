print("\tLogin") #// Getting User Info //#
username = input("Username: ")
password = input("Password: ")

if username == "olamide" and password == "ola123":  #// Verify User Info //#
    print("Login Successful")
else:
    print("Invalid Username or Password")