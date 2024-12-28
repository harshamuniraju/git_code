# # # x=int(input("enter the 1st number"))
# # # y=int(input("enter the 2nd number"))
# # # try:
# # #     result=x/y
# # # except ZeroDivisionError:
# # #     print("zero is not divesible")
# # # else:
# # #     print(f"{result}")
# # # finally:
# # #     print("division")
    
# # total=0
# # count=0
# # while True:
# #     num=input("enter the number")
# #     if num=="done":
# #         print(f"total {total}")
# #         print(f"count {count}")
# #         print(f"average {total/count}")
# #         break
# #     else:
# #         try:
# #             total +=float(num)
# #         except:
# #             print("invalid num")
# #             continue
# #         count +=1

# for i in range(1,6):
#     for j in range(i):
#         print(i)
#     print()
    
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j)
#     print()

start=100
end=200
total=0
current_number=start
while current_number<=end:
    if current_number%2==0:
        total +=current_number
    current_number +=1
print(f"total {total}")