# # # def common_character(string1,string2):
# # #     for latter in string1:
# # #         if latter in string2:
# # #             print(f"common latters {latter} found")
# # # def main():
# # #     common_character("ranjitha","harsha")
    
# # # if __name__=="__main__":
# # #     main()

# # def main():
# #     string=input("enter the string")
# #     vowles=0
# #     consonants=0
# #     blanks=0
# #     for each_character in string:
# #         if (each_character=="a" or each_character=="e" or each_character=="i" or each_character=="o" or each_character=="u"):
# #             vowles+=1
# #         elif "a"<each_character<"z":
# #             consonants+=1
# #         elif each_character==" ":
# #             blanks+=1
# #     print(f"total number of vowles {vowles}")
# #     print(f"total number of conosanats{consonants}")
# #     print(f"total number of blanks {blanks}")
        
# # if __name__=="__main__":
# #     main()

# def main():
#     string=input("enter the string")
#     count_character=0
#     for each_character in string:
#         count_character+=1
#     print(f"leangth of character {count_character}")
# if __name__=="__main__":
#     main()

def strin_processing(user_string):
    
    words=0
    digites=0
    upper=0
    lower=0
    for each_character in user_string:
        if user_string.isdigit():
            digites +=1
        elif user_string.isspace():
            words +=1
        elif user_string.isupper():
            upper +=1
        elif user_string.islower():
            lower +=1
        else:
            pass
    print(f"total number of words{words +1}")
    print(f"total number of digits{digites}")
    print(f"total number of upper laters {upper}")
    print(f"total number of lower laters{lower}")
def main():
    user_string=input("enter the string")
    strin_processing(user_string)
    
    
if __name__=="__main__":
    main()
    
    
# def string_processing(user_string):

#     word_count = 0   
#     digit_count = 0
#     upper_case_count = 0
#     lower_case_count = 0
#     for each_char in user_string:
#         if each_char.isdigit():
#             digit_count += 1
#         elif each_char.isspace():
#             word_count += 1
#         elif each_char.isupper():
#             upper_case_count += 1
#         elif each_char.islower():
#             lower_case_count += 1
#         else:
#             pass
#     print(f"Number of digits in sentence is {digit_count}")
#     print(f"Number of words in sentence is {word_count + 1}")
#     print(f"Number of upper case letters in sentence is {upper_case_count}")
#     print(f"Number of lower case letters in sentence is {lower_case_count}")
# def main():  
#     user_input = input("Enter a sentence ")
#     string_processing(user_input)
# if __name__ == "__main__":
   
#     main()