# # # # print("start")
# # # # for i in range(3):
# # # #     print(f"{i}")
# # # # print("start""stop")
# # # # for i in range(2,5):
# # # #     print(f"{i}")
# # # # print("satart""stop""step")
# # # # for i in range(1,3,5):
# # # #     print(f"{i}")

# # # for each_character in "blue":
# # #     print(f"{each_character}")

# # number=int(input("enter the number"))
# # odd=0
# # even=0
# # for i in range(number):
# #     if i%2==0:
# #         even=even+i
# #     else:
# #         odd=odd+i
# # print(f"sum of even numbers {even} and odd numbver{number}")

# number=int(input("enter the number"))
# fact=1
# if fact<0:
#     print("number is nagative")
# elif fact==0:
#     print("fact 0f 0 is 1")
# else:
#     for i in range(1,number+1):
#         fact=fact*i
# print(f"factorial od {number} is {fact}")

n=0
while True:
    print(f"the value of {n}")
    n=n+1
    if n>5:
        print("the value of n is above five")
        break