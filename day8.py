# # # def world_war():
# # #     allaiance_world_war=input("which alliance win world war")
# # #     year_of_world_war=input("in which year the 2nd world war end")
# # #     return allaiance_world_war,year_of_world_war
# # # def main():
# # #     allaiance,year_of=world_war()
# # #     print(f"world war was won by {allaiance} in the {year_of}")
# # # if __name__=="__main__":
# # #     main()

# # test_veriable=10
# # def outer_function():
# #     test_veriable=50
# #     def inner_function():
# #         test_veriable=100
# #         print(f"this is local varible{test_veriable}")
# #     inner_function()
# #     print(f"this is local variable{test_veriable}")
# # outer_function()
# # print(f'{test_veriable}')    

# def add_cube(a,b):
#     def cube_surface(x):
#         return 6*pow(x,2)
#     return cube_surface(a)+cube_surface(b) 
# def main():
#     result=add_cube(2,3)
#     print(f"surface area of 2 cubes {result}")
# if __name__=="__main__":   
#     main()

def a(prompt,domain="Data Analatices"):
    print(f"{prompt},{domain}")
def main():
    a("sam has intrest in")
    a("harsha has intrest in","cloud computing")
if __name__=="__main__":
    main()4.7