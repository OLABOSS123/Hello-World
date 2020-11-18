#// This is a code to greet greet//#
print("\t\tGreeter v1.0.")
name = input("\tHello User\nPlease, enter your name: ")
time = float(input("What is the time: "))
if time <=12.59:
    print(f"Good morning, {name}.")
elif time >12.59 and time <= 16.59:
    print(f"Good Afternoon, {name}.")
elif time >=16.5 and time <=20.0:
    print(f"Good Evening, {name}.")
elif time >=20.0 and time <=24:
    print(f"Good Night, {name}")
else:
    print(f"\t{name}, enter  a valid input\nPlease enter 24 hours time.")