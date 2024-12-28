# # oceen_animals=("bluewhale","shark","seal")
# # for each in oceen_animals:
# #     print(each
# #           )

# tuple_item=()
# total_item=int(input("enter the number"))
# for i in range(total_item):
#     user_input=int(input("enter the input"))
#     tuple_item+=(user_input,)
# print(f"item is {tuple_item}")

def main():
    a=input("ENTER THE NUMBER")
    b=input("enter the number")
    a,b=b,a
    print("after swapping")
    print(f"value of {a}")
    print(f"value of {b}")
if __name__=="__main__":
    main()