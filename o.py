i = 1
Number = 100
count = 0
while i <= 100:
	if i % 2 == 0:
		print(i, "is an even number.")
	elif i % 2 == 1:
		print(i,"is an odd number.")
        else: 
            for i in range(2, (Number//2 + 1)):
		        if(Number % i == 0):
			        count = count + 1
			        break

	    if (count == 0 and Number != 1):
		    print(Number,"is a Prime Number")
	    else:
			print(Number,"is not a Prime Number")
i = i + 1

	
		



# Number = int(input(" Please Enter any Number: "))
# count = 0

# for i in range(2, (Number//2 + 1)):
#     if(Number % i == 0):
#         count = count + 1
#         break

# if (count == 0 and Number != 1):
#     print(" %d is a Prime Number" %Number)
# else:
#     print(" %d is not a Prime Number" %Number)

# while True:
# 	line = input(">")
# 	if line.lower() == "done":
# 		break
# 	print(line)
# 	print("Done!")


# number = number = eval(input('Please enter a number:'))

# i = 2
# toggle = 0

# while i<number:
# 	if number%i == 0:
# 		toggle = 1
# 	print ("Your number is NOT a prime number!");
# 	i = i + 1
# 	if toggle == 0:
# 		print ("Your number is a prime number!");




# user_name = input("Enter name: ")
# while True:
# 	num_test = int(input("Enter number ? : "))
# 	if num_test == 0:
# 		break
# 	elif num_test != 0:
# 		print(num_test)
# 	if num_test <=2:
# 		print("Too Small")
# 	else:
# 		sum = 0
# 		count = 1

# 		while count <= num_test:
# 			score = int(input("Enter score:"))
# 			sum += score 
# 			decision = str(input("Type Stop!!! \n> "))
# 			if decision.lower() == "stop":
# 				break
# 		avg = sum/count
# 		print(avg)

# import random

# names = ["Olamide","Jones","Chuks","Martins","Coldshot","Ifanyi","Joseph"]
# print(random.shuffle(names))

i = 10
