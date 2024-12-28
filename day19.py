# # # def return_multilple_value():
# # #     monument=input("enter the monument you like")
# # #     year=input("enter the year it was construceted")
# # #     return monument,year
# # # def main():
# # #     mon,yr=return_multilple_value()
# # #     print(f" my favriot {mon} is constructed in {yr}")
# # #     result=return_multilple_value()
# # #     print(f" the {result[0]} and was construceted in {result[1]}")
# # # if __name__=="__main__":
# # #     main()
    
# # def soreted_word(user_input):
# #     list_of_word=user_input.split()
# #     words=list()
# #     for each_word in list_of_word:
# #         words.append((len(each_word),each_word))
# #     words.sort(reverse=True) 
# #     print("after sorting")
# #     for length,word in words:
# #         print(f" the word {word} is at {length}")
# # def main():
# #     sentence=input("enter the the sentence")
# #     soreted_word(sentence)
# # if __name__=="__main__":
# #     main()
    
# def unique_word(*all_word):
#     for each_word in all_word:
#         unique_each_word=list(set(each_word))
#     print(f" unique word {each_word} and its each word is {unique_each_word}")
# def main():
#     unique_word("harsha","ranjitha","arun")
# if __name__=="__main__":
#     main()

def unique_word(user_input):
    words=user_input.split()
    print(f" the words are splited into {sorted(list(set(words)))}")
def main():
    sentence=input("enter the sentence ")
    unique_word(sentence)
if __name__=="__main__":
    main()