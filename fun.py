# def ask_name():
#     name = "Olasco"
#     print("Hello User")
#     name = str(input("What is your name please: "))
#     print(f"Good Morning {name}")
# ask_name()


# def temp_converter(deg_Celsius):
#     """This is a function that converts celcius to fareheight"""
#     c = float(input("Enter your temperature: "))
#     f = (c * 9 /  5 + 32)
#     return f

# name = ask_name()
# f = temp_converter(67)
 
# print(f"{name} converted 67c to {temp_converter()}f.")

# print("hello ")


# def guess():
#     guess = float(input("Enter a number: " ))
#     return guess
#     if guess == 45:
#         print("Winner!!!")

# guess()



# def max_num():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))
#     print(max(num1 , num2 ,num3),"is the largest number")

# max_num()

# def job_qualify():
#     print("\tJob Checker v1.0\nHello User")
#     name = input("What is your name?: ")
#     gender = input("What is your gender: ")
#     if gender.lower() == "male" or gender.lower() == "m":
#         age = int(input(f"{name} enter your Age: "))
#         marital = input("What is your marital status(M/S): ")
#         if age >= 20 and age <= 40:
#             print(f"{name}, you can work in both Urban and Rural areas.")
#         elif age >= 40 and age <= 60:
#             print(f"{name}, you can only work in Urban areas.")
#         else:
#             print("You are not quaalified fot this Service.") 
#     elif gender.lower() == "female" or gender.lower() == "f":
#         marital = input("What is your marital status(M/S): ")
#         age = int(input(f"{name} enter your Age: "))
#         print(f"{name}, you would be working in Urban areas.")
#     else:
#         print("Invalid Input\nEnter either (male/m) or (female/f)")

# job_qualify()


# def   net_salary():
#     print("\tNet salary Checker v1.0\nHello user")
#     name = input("Enter your name: ")
#     salary = float(input(f"{name}, enter your salary: "))
#     year = int(input(f"{name}, how many years have you worked in this company?: "))
#     net_salary = ((0.05)*salary)+salary
#     if year >= 6:
#         print(f"{name}, we are giving you an intrest of 5%\nYour net salary wil be {net_salary}.")
#     else:
#         print(f"{name}, your salary remains {salary}.") 

#     print("Hello World")

# net_salary()

# def salary():
#     salary = float(input(f"{name}, enter your salary: "))
    
# def year():
#     year = int(input(f"{name}, how many years have you worked in this company?: "))

# def salary_out():
#     net_salary = ((0.05)*salary)+salary
#     if year >= 6:
#         print(f"{name}, we are giving you an intrest of 5%\nYour net salary wil be {net_salary}.")
#     else:
#         print(f"{name}, your salary remains {salary}.") 



# def net_salary2():
#     print(salary())
#     print(year())
#     print(salary_out())

# print("\tNet salary Checker v1.0\nHello user")
# name = input("Enter your name: ")
# net_salary2()


# def my_fun(*kid):
#     print("The youngest kid is " + kid[2] + " and " + kid[0] + ".")

# my_fun("Ola", "chuks", "aliyah")



# def my_function(**kid):
#   print("His last name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def greet_user("Olamide"):
#     return "My name is " + "Olamide"

# greet_user()

# def even_odd(x):
#     if x % 2 == 0:
#         print("Number is even") 
#     else:
#          print("Number is odd")
# # even_odd(5)

# def high_num(a,b,c):
#     if a > b and a > c:
#         print(a ,"is the highest number")
#     elif b > a and b > c:
#         print(b ," is the highest number")
#     elif c > a and c > b:
#         print(c ,"is the highest number")

# high_num(2,7,9)    


#  def add(a,b):
#      return a / b

# sum = add(12,4)
# print(sum)

# def height(**kids):
#     print("The tallest kid is " + kids["tname"])

# height(fname= "ola", sname= "bola", tname= "tola", lname= "wale")







# def avg_score(a,b,c,d):
#     total_sum=a+b+c+d  
#     total =total_sum/4
#     print(total)
#     if total >=50:
#         print ('Well done')
#     else:
#         print ('Redo exam')

    
# avg_score(50,60,70,60)




