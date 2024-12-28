# # number=int(input("enter the number"))
# # #number2=input("entre the number")
# # prime=True
# # while number!="enter":
# #     for i in range(2,number):
# #         if number%i==0:
# #             prime=False
# #             break
# #     if prime:
# #         print(f"{number} is prime number")
# #     else:
# #         print(f"{number} is not  prime number")
# #     number=int(input("enter the number"))

# # n=10
# # while n>0:
# #     print(f"current number is{n}")
# #     if n==5:
# #         print(f"number stopes at{n}")
        
# #         n=10
# #         continue
# #     n=n-1
    
# n = 10
# while n > 0: 
#     print(f"The current value of number is {n}")
#     if n==5:
#         print(f"Breaking at {n}")
#         n=10
#         continue
#     n=n-1

while True:
    try:
        number=int(input("enter ther number"))
        print(f"you have enter the {number}")
    except ValueError:
        print("oops enter number")