# # number=int(input("enter the number"))
# # result=0
# # reminder=0
# # while number!=0:
# #     reminder=number%10
# #     result=result+reminder
    
# #     number=int(number/10)
# # print(f"sum of {number} is {result}

# nterms=int(input("enter the number"))
# current=0
# count=0
# previous=1
# next_term=0
# if nterms<=0:
#     print("number is nagative")
# elif nterms==1:
#     print("fabnoic number")
#     print("0")
# else:
#     print("fabnoic series")
#     while count<nterms:
#         print(next_term)
#         current=next_term
#         next_term=previous+current
#         previous=current
#         count+=1
        
largest_number=int(input("enter he number"))
check_number=input("enter the number to check it is large or not")
while check_number!="exit":
    if largest_number>int(check_number):
        print(f"{largest_number} number is larger then {check_number}")
    elif largest_number==int(check_number):
        print(f"largest number{largest_number} is equal to{check_number}")
    elif largest_number<int(check_number):
        print(f"{check_number} is grater then {largest_number}")
    check_number=input("enter the number to check it is large or not")3.13
    
    total=0
count=0
while True:
    num=input("enter the number")
    if num=="done":
        print(f"total {total}")
        print(f"count {count}")
        print(f"average {total/count}")
        break
    else:
        try:
            total +=float(num)
        except:
            print("invalid num")
            continue
        count +=1l