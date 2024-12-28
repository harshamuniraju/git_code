# # def employee(employee_number):
# #     employee_name=dict()
# #     for i in range(1,employee_number+1):
# #         name=input("enter the employee name")
# #         number=input("enater the employee id numer")
# #         salary=int(input("enter the employee salary"))
# #         employee_name[name]=[number,salary]
# #     employee_search=input("enter the name of employee to search")
# #     if employee_search not in employee_name:
# #         print(f"employee {employee_search} not found") 
# #     else:
# #         print(f" here the information about {employee_search}")
# #         print(f"employee Id {number}")
# #         print(f"salary {salary}") 
# # def main():
# #     employee_number=int(input("enter the number of employee"))
# #     employee(employee_number)
# # if __name__=="__main__":
# #     main()  
    
# def main():
#     country={"India":"Delhi","Amrica":"Landon","Russia":"france"}
#     for key,value in sorted(country.items()):
#         print(key,value)
# if __name__=="__main__":
#     main()
    
def frnd(number):
    frnd_name=dict()
    for i in range(number):
        name=input("enter the name ")
        number=int(input("enter the phone number "))
        frnd_name=name
    for name,number in sorted(frnd_name.items):
        print(f" name {name}")
        print(f" number {number}")
def main():
    number=int(input("enter the number of contect"))
    frnd(number)
if __name__=="__main__":
    main()