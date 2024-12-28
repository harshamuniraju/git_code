# # # food=['rice','gobi','roti','panner']
# # # for each_food in food:
# # #     print(f"i love to eat {each_food}")

# # exlore=['google','chrome','firefox']
# # for each_value in range(len(exlore)):
# #     print(f"this are explorer we use '{exlore[each_value]}' at {each_value}")

# matrix=[[10,20],[30,40],[50,60]]
# matrix_transport=[[0,0,0],[0,0,0]]
# def main():
#     for rows in range(len(matrix)):
#         for columns in range(len(matrix[0])):
#             matrix_transport[columns][rows]=matrix[rows][columns]
#     print("matrix transportation")
#     for item in matrix_transport:
#         print(f"matrix={item}")
# if __name__=="__main__":
#     main()

matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[10,11,12],[13,14,15],[16,17,18]]
matrix_result=[[0,0,0],[0,0,0],[0,0,0]]
def main():
    for rows in range(len(matrix1)):
        for columns in range(len(matrix2[0])):
            matrix_result[rows][columns]=matrix1[rows][columns]+matrix2[rows][columns]
    print("matrix")
    for item in matrix_result:
        print(item)
if __name__=="__main__":
    main()