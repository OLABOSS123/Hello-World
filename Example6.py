import time

#-----------------Asks for the dacision of the User------------------#
def quest1():
    f = open(file_name)
    print("Please wait, operning file..........")
    time.sleep(2)
    write_or_not = input("Do you want to write in the file, Yes or No: ")
    if write_or_not=="yes":
        while write_or_not=="yes":
            what_to_write = input("Enter what to write in the file: ")

            if what_to_write=="done":
                break
            else:
                f.write(what_to_write)
                f.write("\n")
        f.close()

#-----------------Decision after the reply from the User-----------#
def except1():
    print("Loading..........")
    time.sleep(2)
    choice = input("Your file does not exist, Do you want to create a file, Yes or No: ")
    if choice=="yes":
        f = open(file_name, "x")
        print("Loading.......")
        time.sleep(2)
        print("Your requested file was created.")
        write_or_not = input("Do you want to write in the file, Yes or No: ")
        if write_or_not=="yes":
            while True:
                what_to_write = input("Enter what to write in the File: ")
                if what_to_write=="done":
                    break
                else:
                    f.write(what_to_write)
                    f.write("\n")
            f.close()                
        else:
            while write_or_not=="no":
                print("Will not write in new File.")
                break
    
        
        while choice == "no":
            print("Your requested file was not created.")
            break

#-------Main Code------#
name = input("Enter your name please: ")
print(f"\t Welcome {name}\n\t File Creator v1.0")
file_name = input("Enter filename or filename to create: ")
try:
    quest1()
except FileNotFoundError:
    except1()
finally:
    print("Your file has been appended.")

