# # def red_file():
# #     file_handler=open("c:\plearn\av.text")
# #     print(" printing each line in file")
# #     for each_line in file_handler:
# #         print(each_line)
# #     file_handler.close()
# # def main():
# #     red_file
# # if __name__=="__main__":
# #     main()

# def read_file():
#     # with open("C:/Users/harsh/OneDrive/Desktopab.txt") as file_handeler:
#         for each_line in file_handeler:
#             print(each_line,end="")
# def main():
#     read_file()
# if __name__=="__main__":
#     main()
def main():
    with open("C:/Users/harsh/OneDrive/Desktop/ab.txt") as file_handeler:
        print(file_handeler.read(),end="")
if __name__=="__main__":
    main()