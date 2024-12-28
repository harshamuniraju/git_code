# # # # def last_string(string):
# # # #     return string[len(string)-1]
# # # # my_string="hellow world"
# # # # last_character=last_string(my_string)
# # # # print(f"the last character is{last_character}")

# # # def main():
# # #     string=input("enter the string")
# # #     no=int(input("enter the number of times to print"))
# # #     a=string*no
# # #     print(f"{a}")
# # # if __name__=="__main__":
# # #     main()

# # def dob(date):
# #     h=date.split("/")
# #     new="-".join(h)
# #     print(new)
# # def main():
# #     my_date=input("enter you date of month")
# #     dob(my_date)
# # if __name__=="__main__":
# #     main()

# def con(str1,str2):
#     return "".join([str1,str2])
# str1=input("enter the string 1")
# str2=input("enter the string 2")
# result=con(str1,str2)
# print(f"after concationation {result}")

def extract_first_term(string,n):
    return string[:n]
string=input("enter the string")
n=int(input("enter the number of character"))
result=extract_first_term(string,n)
print(f"the number {n} of chaaracter are {result}")