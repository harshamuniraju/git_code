# # # a="harsha"
# # # b="bhumi"
# # # print(a==b)

# # word="abcdefghij"
# # print(word[0:7:2])

# def main():
        
#     string=input("enter the string")
#     while string!=0:
#         if string==string[::-1]:
#             print("string is palandrom")
#         else:
#             print("string is not palandrom")
#         string=input("enter the string")
# if __name__=="__main__":
#     main()

def main():
    string="google"
    print(f"string is {string}")
    index=0
    for each_charcter in string:
        print(f"the word is {each_charcter} of index {index}")
        index +=1
if __name__=="__main__":
    main()5.3