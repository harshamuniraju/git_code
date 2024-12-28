# # # currency={'India':'rupees','amrica':'dollar','japan':'yen','rusia':'rubi','garmany':'euro'}
# # # def main():
# # #     print("countries")
# # #     for key in currency.keys():
# # #         print(key)
# # #     for value in currency.values():
# # #         print(value)
# # #     for key,value in currency.items():
# # #         print(f" this particular countries {key} has currencay in {value}")
# # # if __name__=="__main__":
# # #     main()

# # history={'India':1947,'paksithian':1948,'china':1950}
# # def check_key():
# #     key=input("enter the country ")
# #     if key in history.keys():
# #         print(f"{key} has got freedom")
# #     else:
# #         print(f"{key} this particular country has not got freedom")
# # def sum_check():
# #     print(f"sum of values are")
# #     print(f"{sum(history.values())}")
# # def main():
# #     check_key()
# #     sum_check()
# # if __name__=="__main__":
# #     main()

# books=["abcd","abcd","dad","dad","tree"]
# def main():
#     count_item=dict()
#     for book_name in books:
#         count_item[book_name]=count_item.get(book_name,0)+1
#         print("the book are")
#         print(count_item)
# if __name__=="__main__":
#     main()

def main():
    count_word=dict()
    sentence=input("enter the sentence ")
    for each_word in sentence:
        count_word[each_word]=count_word.get(each_word,0)+1
    print("this are the wors repated")
    print(count_word)
if __name__=="__main__":
    main()