list1 = []
print("\tHello User\n---------Average Calculator-----------")
try:
    count = 0
    length = int(input("How many numbers do you want to add?: "))
    while count < length:
        numbers = int(input("Enter a number: "))
        list1.append(numbers)
        count += 1
        avg = sum(list1)/len(list1)
    print(avg)
except ValueError:
    print("Enter an integer!!!: ")



