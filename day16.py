# # # # def constracter_character_dict(word):
# # # #     count_character_dict=dict()
# # # #     for each_character in word:
# # # #         count_character_dict[each_character]=count_character_dict.get(each_character,0)+1
# # # #     sorted_key=sorted(count_character_dict.keys())
# # # #     for each_key in sorted_key:
# # # #         print(each_key,count_character_dict.get(each_key))
# # # # def main():
# # # #     word=input("enter the string")
# # # #     constracter_character_dict(word)    
# # # # if __name__=="__main__":
# # # #         main()
    
# # # def main():
# # #     number=int(input("enter the number"))
# # #     number_count_dict=dict()
# # #     for i in range(1,number+1):
# # #         number_count_dict[i]=i*i
# # #     print("the dictoioranary is")
# # #     print(number_count_dict)
# # # if __name__=="__main__":
# # #     main()

# # def main():
# #     sentence=input("enter the number")
# #     count_character={"digites":0,"upper":0,"lower":0}
# #     for each_character in sentence:
# #         if each_character.isdigit():
# #             count_character["digites"]+=1
# #         elif each_character.isupper():
# #             count_character["upper"]+=1
# #         elif each_character.islower():
# #             count_character["lower"]+=1
# #     print("the characters are in")
# #     print(count_character)
# # if __name__=="__main__":
# #     main()
    
# def student_details(student_number):
#     student_name={}
#     for i in range(0,student_number):
#         name=input("enter the name of student")
#         rool_no=input("enter the rrigister number of the student")
#         marks=int(input("enter the total marks of student"))
#         student_name[name]=[rool_no,marks]
#     student_search=input("enter the name of the student you want to search")
#     if student_search not in student_name.keys():
#         print(f"the student {student_search} not foud")
#     else:
#         print(f"the student details are hear")
#         print(f"rigister number {student_name[student_search][0]}")
#         print(f"the total marks of student is {student_name[student_search][1]}")
# def main():
#     student_number=int(input("enter the number of student"))
#     student_details(student_number)
# if __name__=="__main__":
#     main()

def main():
    student_details={"name":"harsha","roll_no":15,"marks":{"python":56,"java":30,"html":56}}
    print(student_details["name"])
    print(student_details["roll_no"])
    average=sum(student_details["marks"].values())/len(student_details["marks"])
    print(f"total marks is {average}")
if __name__=="__main__":
    main()