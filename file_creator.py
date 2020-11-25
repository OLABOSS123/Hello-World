import time
print("\tWElcome")
name = input("Enter your name please: ")
print(f"\tHello , {name}\nThis is a program that allows you to create a file and write in it")
start = input("Enter start to continue: ")
if start.lower() == "start":
    print("Let's procede........")
    time.sleep(2)
    ask = input("Enter the name of the file you want to create: ")
elif start.lower() != "start":
    print("Type start to continue!!!")
try:
    create = open(f"{ask}","x")
except FileExistsError:
    print("File already exists")
    write1 = open(ask,"w")
    write = str(input("Enter what you wounld like to write in the file: "))
    write1.write(write)
    print("Done!!!\n\tSuccessfull")
else:
    create_write = open(ask,"w")
    write = str(input("Enter what you wounld like to write in the file: "))
    create_write.write(write)
    print("Done!!!\n\tSuccessfull")