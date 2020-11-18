#// PYSTORE//#
print("\tWelcome to Pystore")
name = input("Enter your name please: ")
purchase = input(f"{name}, What would you like to purchase please\n(1)Phone(s)\n(2)Car(s)\n(3)Shade(s)\n> ")
if  purchase.lower() == "phone" or purchase == "1" or purchase.lower() == "phones":
    brand = input(f"\tWe have brands like:\n(1)Samsung\n(2)Tecno\n{name}, Which type of brand would you like to purchase?: ")
    if brand.lower() == "samsung":
        print(f"\t{name},These are the lists of Samsung Smartphones we sell in Pystore.\n(1)Samsung J5\n(2)Samsung J6\n(3)Samsung J7\n(4)Samsung S10\n(5)Samsung S20")
        choose = input(f"{name}, Choose your prefered phone to purchase: ")
        #\\ SAMSUNG \\#
        if choose == "1" or choose.lower() == "samsung j5" or choose.lower() == "samsungj5" :
            price = 55000
            quantity = int(input(f"{name}, How many Samsung J5 would you like to purchase: "))
            if quantity == 2:
                tprice = (price * quantity) * 0.2
                dprice = (tprice - price)
                print(f"{name} You had a discount of 20%, and your bill is {dprice}.")
            else:
                bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
                print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "samusng j6" or choose.lower() == "samsungj6":
            price = 89000
            quantity = int(input(f"{name}, How many Samsung J6 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "samsung j7" or choose.lower() == "samsungj7":
            price = 150000
            quantity = int(input(f",{name}, How many Samsung J7 would you like to purchase: "))
            bill = f"{name},Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "samsung s10" or choose.lower() == "samsungs10":
            price1 = 472527
            quantity = int(input(f"{name}, How many Samsung S10 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "samsung s20" or choose.lower() == "samsungs20":
            price1 = 500000
            quantity = int(input(f"{name}, How many Samsung S20 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")
        #\\ TECNO \\#
    elif brand.lower() == "tecno":
        print(f"\t{name}, These are the lists of Tecno Smartphones we sell in Pystore\n(1)Techo Camon 12 PRO\n(2)Tecno Spark 4\n(3)Tecno Camon 15\n(4)Tecno Spark 5\n(5)Tecno Pouvoir 4")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "techo camon 12 pro" or choose.lower() == "techocamon12pro":
            price = 58500
            quantity = int(input(f"{name}, How many Techo Camon 12 PRO would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "tecno spark 4" or choose.lower() == "tecnospark4" :
            price = 43500
            quantity = int(input(f"{name},How many Tecno Spark 4 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "tecno camon 15" or choose.lower() == "tecnocamon15":
            price = 63413
            quantity = int(input(f"{name}, How many Tecno Camon 15 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "tecno spark 5" or choose.lower() == "tecnospark5":
            price = 47500
            quantity = int(input(f"{name}, How many Tecno Spark 5 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "tecno pouvoir 4" or choose.lower() == "tecnopouvoir4":
            price = 50000
            quantity = int(input(f"{name}, How many Tecno Pouvoir 4 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number")
            #\\ CARS \\#
elif purchase.lower() == "2" or purchase.lower() == "car" or purchase.lower() == "2" or purchase.lower() == "cars": 
    print("\tNote: WE ONLY SELL OUR CARS IN DOLLARS")
    brand = input(f"{name}, Which brand or Cars would you like to purchase?: ")
    if brand.lower() == "toyota":
        print(f"\t{name},These are the lists of Toyota Cars we sell in Pystore.\n(1)Toyata Corolla 2005\n(2)Toyota Yaris\n(3)Toyota Yaris Hatchback\n(4)Toyota Corolla Hybrid\n(5)Toyota Prius")
        choose = input(f"{name}, Choose your perfered Car to purchase: ")
        if choose == "1" or choose.lower() == "toyota corolla 2005" or choose.lower() == "toyotacorolla2005" :
            price = 19825
            quantity = int(input(f"{name}, How many Toyata Corolla 2005 would you like to purchase: "))
            bill = f"{name}, Your bill is ${price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "toyota yaris" or choose.lower() == "toyotayaris":
            price = 15650
            quantity = int(input(f"{name}, How many Toyota Yaris would you like to purchase: "))
            bill = f"{name}, Your bill is ${price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "toyota yaris hatchback" or choose.lower() == "toyotayarishatchback":
            price = 15650
            quantity = int(input(f",{name}, How many Toyota Yaris Hatchback would you like to purchase: "))
            bill = f"{name},Your bill is ${price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "toyota corolla hybrid" or choose.lower() == "toyotacorollahybrid":
            price = 23400
            quantity = int(input(f"{name}, How many Toyota Corolla Hybrid would you like to purchase: "))
            bill = f"{name}, Your bill is ${price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "toyota prius" or choose.lower() == "toyotaprius":
            price = 24525
            quantity = int(input(f"{name}, How many Toyota Prius would you like to purchase: "))
            bill = f"{name}, Your bill is ${price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")
        #\\ SHADES \\#
elif  purchase.lower() == "shades" or purchase == "3" or purchase.lower() == "shade":
        print(f"\t{name},These are the lists of Samsung Smartphones we sell in Pystore.\n(1)Tom Ford\n(2)Thom Browne\n(3)Saint Laurent\n(4)Ray Ban\n(5)Persol")
        choose = input(f"{name}, Choose your prefered Shades to purchase: ")
        if choose == "1" or choose.lower() == "tom ford" or choose.lower() == "tomford" :
            price = 25000
            quantity = int(input(f"{name}, How many Tom Ford would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "thom browne" or choose.lower() == "thombrowne":
            price = 35000
            quantity = int(input(f"{name}, How many Thom Browne would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "saint laurent" or choose.lower() == "saintlaurent":
            price = 15000
            quantity = int(input(f",{name}, How many Saint Laurent would you like to purchase: "))
            bill = f"{name},Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "ray ban" or choose.lower() == "ray ban":
            price = 47252
            quantity = int(input(f"{name}, How many Ray Ban would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "presol":
            price = 50000
            quantity = int(input(f"{name}, How many Persol would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")