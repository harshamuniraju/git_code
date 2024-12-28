# # def case_convertion(user_string):
# #     case_convertion=str()
# #     for each_character in user_string:
# #         if each_character.isupper():
# #             case_convertion += each_character.lower()
# #         else:
# #             case_convertion += each_character.upper()
# #     print(f"modified string is{case_convertion}")
    
# # def main():
# #     user_string=input("entre the string")
# #     case_convertion(user_string)
# # if __name__=="__main__":
# #     main()
    
# def replace(comma_supprate_word):
#     word=comma_supprate_word.split(",")
#     word.sort()
#     hyphen_supprate_word="-".join(word)
#     print(f"the replace word is{hyphen_supprate_word}")
# def main():
#     comma_supprate_word=input('enter the string') 
#     replace(comma_supprate_word)
# if __name__=="__main__":
#     main()   

def word_count(word_occurance,user_string):
    count_word=0
    for each_word in user_string.split():
        if each_word==word_occurance:
            count_word += 1
    print(f"the {word_occurance} and the occurance of {count_word} times")
def main():
    input_string=input("enter the string")
    
    word_occurance=input("enter the word")
    word_count(word_occurance,input_string)
if __name__=="__main__":
    main()