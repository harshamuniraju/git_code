# # # year=int(input("enter the year"))
# # # if year%4==0:
# # #     if year%100==0:
# # #         if year%400==0:
# # #             print(f"{year} is leap year")
# # #         else:
# # #             print(f"{year} is not leap year")
# # #     else:
# # #         print(f"{year} is leap year")
# # # else:
# # #     print(f"{year} is not leap year")

# # i=0
# # while i<10:
# #     print(f"i is {i}")
# #     i=i+1

# num=int(input("enter the number"))
# i=0
# sum=0
# count=0
# while i<num:
#     i=i+1
#     sum=sum+i
#     count=count+1
# avg=sum/count
# print(f"average of {num} is {avg}")

n=int(input("enter the first number"))
m=int(input("enter the second number"))
if n==0 and m==0:
    print("number is invalid")
if n == 0:
    print(f"gcd {m}")
if m == 0:
    print(f"gcd {n}")
while n != m:
    if n > m:
        n = n-m
    if m >n:
        m = m-n
print(f"gcd of is {n}")

# m = int(input("Enter first positive number"))
# n = int(input("Enter second positive number"))
# if m == 0 and n == 0:
#     print("Invalid Input")
# if m == 0:
#     print(f"GCD is {n}")
# if n == 0:
#     print(f"GCD is {m}")
# while m != n:
#     if m > n:
#         m = m - n
#     if n > m:
#         n = n - m
# print(f"GCD of two numbers is {m}")