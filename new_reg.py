import time
# User registration
users ={}
new_user_registration ={}
user_info = "Name","Username"
verify = "Password" , "Confirm your Password"

i = 0
while i < len(user_info):
    info = input(f"Enter your {user_info[i]}: ")
    new_user_registration.update({user_info[i]:info})
    i+=1

t = 0
ent1 = input(f"Enter your {verify[t]}: ")
while t < len(verify):
    ent2 = input(f"Please {verify[1]}: ")
    if ent1 == ent2:
        new_user_registration.update({verify[t]:ent1})
        print("Account Created successfully!!!")
        break
    else:
        print("\t Invalid Password")
        continue
    t +=1



lo = True
time.sleep(3)
quest = str(input("\n\n\tDo you want to login? :"))
while lo == True:
    if quest.lower() == "yes":
        user = input(f"Enter your {user_info[1]}: ")
        pas = input(f"Enter your {verify[0]}: ")
        if user == new_user_registration["Username"] and pas == new_user_registration["Password"]:
            print("Loading.........")
            time.sleep(5)
            print("\t\tLogin Successfull\n ------------Welcome to Facebook-------------")
            break
        elif user == new_user_registration["Username"] and pas != new_user_registration["Password"]:
            print("Loading.........")
            time.sleep(5)
            print(f"\tInvalid {verify[0]}")
        elif user != new_user_registration["Username"] and pas == new_user_registration["Password"]:
            print("Loading.........")
            time.sleep(5)
            print(f"\tInvalid {user_info[1]}")
        elif user != new_user_registration["Username"] and pas != new_user_registration["Password"]:
            print("Loading.........")
            time.sleep(5)
            print(f"Invalid {user_info[1]} and {verify[0]}")
    elif quest.lower() == "no":
        print("\nThank you for creating an account with us\n\tThanks for using Facebook \n\tBye!!! ")

key = len(users)
key += 1
users.update({key:new_user_registration})
print(users)
