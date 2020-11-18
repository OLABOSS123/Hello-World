#(1)
def remove_first_and_last():
    listname = []
    count = 0
    x = int(input("How many values do you want to insert?: "))
    while count < x:
        value = eval(input("Enter your List value: "))
        append = listname.append(value)
        count += 1
    print(listname[1:x-1])


remove_first_and_last()

# (2)
# def highest_in_list():
#     listname = []
#     count = 0
#     x = int(input("How many values do you want to insert?: "))
#     while count < x:
#         value = eval(input("Enter your List value: "))
#         append = listname.append(value)
#         count += 1
#     listname.sort()
#     print(listname[x-1],)

# highest_in_list()


# (3)
# def multiply_list():
#     listname = []
#     count = 0
#     x = int(input("How many values do you want to insert?: "))
#     while count < x:
#         value = eval(input("Enter your List value: "))
#         append = listname.append(value)
#         count += 1
#     listname.sort()
#     listname = [x * 2 for x in listname]
#     print(listname)

# multiply_list()


#(4)
# def lowest_in_list(one: list,int,str,float):
#     listname = []
#     count = 0
#     x = int(input("How many values do you want to insert?: "))
#     while count < x:
#         value = eval(input("Enter your List value: "))
#         append = listname.append(value)
#         count += 1
#     listname.sort()
#     print(listname[0])
#         return listname[0]


#work = print(listname[0])
#print(work)



# lowest_in_list()


# (5)
# def length_of_word(value):
#     count = 0
#     for t in value:
#            count += 1
#     return count


# work = length_of_word("ola")
# print(work)


# count = []
# greet = "boy"
# for word in greet:
#     append = count.append(word)

# def length_():
#     x = str(input("Enter your Value: "))
#     print(x.count)

# length_()

# Bonus
# def highest_in_list():
#     listname = []
#     count = 0
#     x = int(input("How many values do you want to insert?: "))
#     while count < x:
#         value = eval(input("Enter your List value: "))
#         append = listname.append(value)
#         count += 1
#     listname.sort()
#     result = 1
#     for t in listname:
#         result  = result * t
#         print(result)


# highest_in_list()

# def highest__list():
#     listname = []
#     count = 0
#     x = int(input("How many values do you want to insert?: "))
#     while count < x:
#         value = eval(input("Enter your List value: "))
#         append = listname.append(value)
#         count += 1
#     listname.sort()
#     print(listname[x-1],)

# highest_in_list()

