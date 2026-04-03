# # 1.WAP to accept any positive negative zero 
# no = int(input("Enter any number: "))
# if no > 0:
#     print("Number is positive")
#     if (no == 0):
#         print("Number is zero")
#     print("Number is negative")


# # 2. wap to accept to accecpt max no in 5 values
# val1 = int(input("Enter value of val1: "))
# val2 = int(input("Enter value of val2: "))
# val3 = int(input("Enter value of val3: "))
# val4 = int(input("Enter value of val4: "))
# val5 = int(input("Enter value of val5: "))
# if val1 > val2 and val1 > val3 and val1 > val4 and val1 > val5:
#     print("Max value is: ",val1)
#     if val2 > val1 and val2 > val3 and val2 > val4 and val2 > val5:
#         print("Max value is: ",val2)
#         if val3 > val1 and val3 > val2 and val3 > val4 and val3 > val5:
#             print("Max value is: ",val3)
#             if val4 > val1 and val4 > val2 and val4 > val3 and val4 > val5:
#                 print("Max value is: ",val4)
#                 if val5 > val1 and val5 > val2 and val5 > val3 and val5 > val4:
#                     print("Max value is: ",val5)

# print("Max value is: ",max(val1,val2,val3,val4,val5))




# 3. WAP to accept username and password and check if both are same or not
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == password:
#     print("Login successful")
# else:
#     print("Login failed")


# wap to accept phy chem and math subject marks calculate total and percentage and if percentage is greater than equal to 60 and greater is equal to male so he is eligible for placement else eligible for data entry job

# phy = int(input("Enter marks of physics: "))
# chem = int(input("Enter marks of chemistry: "))         
# math = int(input("Enter marks of maths: "))
# gender = input("Enter your gender(male/female): ")
# total = phy + chem + math
# percentage = total/3.0
# print("Total marks: ", total)
# print("Average marks: ", percentage)
# if percentage >= 60 and gender.lower() == "male":
#     print("Student is eligible for placement")
#     print("Student is eligible for data entry job")
# else:
#     print("Student is not eligible for placement")
#     print("Student is not eligible for data entry job")


# wap to accept valuenof A ,B, C and find max value using nested if else statement
# A = int(input("Enter value of A: "))
# B = int(input("Enter value of B: "))
# C = int(input("Enter value of C: "))
# if A > B:
#     if A > C:
#         print("Max value is: ",A)
#     else:
#         print("Max value is: ",C)
# else:
#     if B > C:
#             print("Max value is: ",B)
#     else:
#         print("Max value is: ",C)
                

#wap to identify working day and hodliday with in inputed day 
# day = input("Enter a day: ").lower()
# if day in ["saturday", "sunday"]:
#     print("It's a holiday")
# else:
#         print("It's a working day")



# wap to check its is lower case upper case or digit or special character
# ch = (input("Enter a character: "))
# ch = ord(ch)
# if ch >= 65 and ch <= 90:
#     print("It's an uppercase letter")
# elif ch >= 97 and ch <= 122:
#     print("It's a lowercase letter")
# elif ch >= 48 and ch <= 57:
#     print("It's a digit")
# else:
#     print("It's a special character")


# WAP  to calculate notes and Coin of 500, 200, 100, 50, 20, 10, 5, 2 and 1 from given amount
# amount = int(input("Enter an amount: "))
# notes_500 = amount // 500
# amount %= 500
# print("Notes of 500: ", notes_500)
# notes_200 = amount // 200
# amount %= 200
# print("Notes of 200: ", notes_200)
# notes_100 = amount // 100
# amount %= 100
# print("Notes of 100: ", notes_100)
# notes_50 = amount // 50
# amount %= 50
# print("Notes of 50: ", notes_50)
# notes_20 = amount // 20
# amount %= 20
# print("Notes of 20: ", notes_20)
# notes_10 = amount // 10
# amount %= 10
# print("Notes of 10: ", notes_10)
# notes_5 = amount // 5
# amount %= print("Notes of 5: ", notes_5)
# notes_2 = amount // 2
# amount %= 2
# print("Notes of 2: ", notes_2)
# notes_1 = amount // 1
# amount %= 1
# print("Notes of 1: ", notes_1)



