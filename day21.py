def main():
    with open("C:/plearn/day20.py") as file_handler:
        for each_row in file_handler:
            each_row=each_row.replace("","#")
            print(each_row,end="")
if __name__=="__main__":
    main()