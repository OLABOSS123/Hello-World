# (5)
# num = int(input ("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FIZZBUZZ")
# elif num % 3 == 0: 
#      print("BUZZ")
# elif num % 5 == 0: 
#     print("FIZZ")


# n = 1 
# incrN = n + 1
# while(n>=100):
#     if (n%2) == 0: 
#         print(n,"is an even number")
#     print(incrN)
#     elif (n%2) == 1: 
#         print(n,"is an odd number")
#     print(incrN)
# else:
#     if (n%3) >= 1:
#         print(n,"is a prime number")
#     print(incrN)


# (1)
def count_letter(word, letter):
    count = 0
    for alpha in word:
        if alpha == letter:
            count += 1
    return count

spell = count_letter("banana","a")
print(spell)




# (3)
# def started(word, letter):
#     for t in word:
#         if word[0] == letter:
#             return ("It started with b")


# check = started("banana","b")
# print(check)



# (4)
# def avg():
#     count = 1
#     ask = eval(input("How many numbers: "))
#     sum_num = 0
#     while count <= ask:
#         num = eval(input("Enter the number: "))
#         sum_num = sum_num + num
#         count += 1
#     avg= sum_num/ask 
#     print("The average is",avg)
        
        
# avg()


# (7)
# notQuit = True
# while notQuit == True:
#     text = str(input("Enter an input: "))
#     if text.lower().__eq__("quit"):
#         notQuit = False
#     else:
#         print(text)

# (2)
# def slicer(word, start,stop):
#     x = (word[start:stop])
#     print (x)

# slicer("banana",0,2)


#(8)
# str = input("Enter a string: ")

# # counter variable to count the character in a string
# counter = 0
# for s in str:
#       counter = counter+1
# print("Length of the input string is:", counter)


# while True:

# 	if n % 2 == 0: 
# 	    print(n,"is an even number.") 
# 	else:
#         	print(n,"is an odd number")
# 	n += 2
	


# while True:
#     text = input("> ")
#     if text.lower() == "quit":
#         break
#     elif text.lower() == "tired":
#         continue
#     else:
#         print(text)
# else:
#     print("This loop is done!!!")


