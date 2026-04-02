# # # # # # # math = 50
# # # # # # # name = "vivek"
# # # # # # # pi = 3.14
# # # # # # # result = True

# # # # # # # type function
# # # # # # # print (type(math))
# # # # # # # print(type(name))
# # # # # # # print(type(pi))
# # # # # # # print(type(result))

# # # # # # # id function
# # # # # # # print (id(math))
# # # # # # # print(id(name))
# # # # # # # print(id(pi))
# # # # # # # print(id(result))

# # # # # # math = 50
# # # # # # chem = 50
# # # # # # print(id(math))
# # # # # # print(id(chem))

# # # # # # list = [[1,2,3],
# # # # # #         [4,5,6],
# # # # # #         [7,8,9]]
# # # # # # for i in list:
# # # # # #     for j in i:
# # # # # #         if i==j:
# # # # # #             sum = sum + list[j][j]


# # # # # print(2+2)
# # # # # print("2"+"2")
# # # # # val1 = (int(input("Enter value of val1: ")))
# # # # # val2 = (int(input("Enter value of val2: ")))
# # # # # print(val1+val2)
# # # # # # # # input function by defaut accept only str value

# # # # # print(int(3.14))
# # # # # # print(int(10+5j)) not possible to convert complex number to int
# # # # # print(int(True))
# # # # # print(int(False))
# # # # # # print (int("4.22")) not possible to convert string with decimal point to int
# # # # # print(int("4"))

# # # # # flot() use to convert
# # # # #print(float(3)) type of 3 is int but after converting it to float it will be 3.0
# # # # #print(float(50+5j)) not possible to convert complex number to float
# # # # print(float(True))  
# # # # print(float(False))
# # # # print(float("4.22"))
# # # # print(float("4"))

# # # # complex() used to convert
# # # # print(complex(3))
# # # # print(complex(12.5))
# # # # print(complex(True)) 
# # # # print(complex(False)) 
# # # # print(complex("5")) 
# # # # print(complex(5.6))
# # # # print(complex(5,-3))
# # # # print(complex(True,False)) 

# # # # bool() is used to convert
# # # # print(bool(0))
# # # # print(bool(15))
# # # # print(bool(3.14))
# # # # print(bool(0.0))
# # # # print(bool(1+2j))
# # # # print(bool(0+0j))
# # # # print(bool("-1"))
# # # # print(bool(False))
# # # # print(bool(True))

# # # # # swap two numbers using 3 variable
# # # # val1 = (int(input("Enter value of val1: ")))
# # # # val2 = (int(input("Enter value of val2: ")))
# # # # print("Before swapping: ", val1, val2)
# # # # temp = val1
# # # # val1 = val2 
# # # # val2 = temp
# # # # print("After swapping: ", val1, val2)

# # # # using 2 vaarial
# # # # val1 = (int(input("Enter value of val1: ")))
# # # # val2 = (int(input("Enter value of val2: ")))
# # # # print("Before swapping: ", val1, val2)
# # # # va1=val1 + val2
# # # # val2=va1-val2
# # # # val1=va1-val2
# # # # print("After swapping: ", val1, val2)


# # # # 3 sub marks
# # # p1 = int(input("Enter marks of physics: "))
# # # p2 = int(input("Enter marks of chemistry: "))   
# # # p3 = int(input("Enter marks of maths: "))

# # # total = p1 + p2 + p3
# # # percentage = total/3.0
# # # print("Total marks: ", total)
# # # print("Average marks: ", percentage)
# # # print("student is fail because he is graduated from ybit")

# # # interest calculator
# # # p_amount = int(input("Enter principal amount: "))
# # # rate = float(input("Enter rate of interest: "))
# # # time = int(input("Enter time in years: "))
# # # simple_interest = (p_amount * rate * time) / 100
# # # print("Simple Interest: ", simple_interest)

# # # height converter feet to inches and cm
# # print("Enter height in feet: ")
# # height = float(input())
# # inches = height * 12
# # cm = inches * 2.54
# # print("Height in inches: ", inches)
# # print("Height in cm: ", cm)

# # # reverse the number
# # num = 123 
# # a = num % 10 
# # num = num // 10
# # b = num % 10
# # c = num % 10
# # rev = a*100 + b*10 + c 
# # print("Reverse of the number: ", rev)


# num =123456
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10   
# print(c) 
# num = num // 10
# print(num)
# d = num % 10
# print(d)
# num = num // 10
# print(num)
# e= num % 10
# print(e)
# num = num // 10
# print(num)
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + num
# print("Reverse of the number: ", rev)


# special operator
# identity operator
# a = 10
# b = 20
# print(a is b)  # False
# print(a is not b)  # True

# membership operator
# name = "vivek"
# print("v" in name)  # True
# print("p" in name)  # False
