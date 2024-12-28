# # def ranj(i,l="smart",o="handsome",v="perfect",e="attitude"):
# #     print(f"harsha {i} is {l} he looks {o} he works {v} and with {e}")
# #     print(f" he has positive {e}")
# #     print(f'he is {v} in his job')
# # ranj("m")
# # ranj("muni raju")
# # ranj(".M")

# n1=float(input("enter the first number"))
# n2=float(input("enter the second number"))
# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2

# print(add(n1,n2))
# print(sub(n1,n2))
# print(mul(n1,n1))
# print(div(n1,n2))
# # def add(a, b):
# #     """Function to add two numbers."""
# #     return a + b

# # def subtract(a, b):
# #     """Function to subtract two numbers."""
# #     return a - b

# # def multiply(a, b):
# #     """Function to multiply two numbers."""
# #     return a * b

# # def divide(a, b):
# #     """Function to divide two numbers."""
# #     if b != 0:
# #         return a / b
# #     else:
# #         return "Division by zero is not allowed"

# # def main():
# #     """Main function to take input and perform operations."""
# #     print("Arithmetic Operations:")
# #     print("1. Addition")
# #     print("2. Subtraction")
# #     print("3. Multiplication")
# #     print("4. Division")

# #     # Take user input
# #     choice = int(input("Enter your choice (1-4): "))
# #     num1 = float(input("Enter the first number: "))
# #     num2 = float(input("Enter the second number: "))

# #     # Perform the chosen operation
# #     if choice == 1:
# #         print(f"The result of addition is: {add(num1, num2)}")
# #     elif choice == 2:
# #         print(f"The result of subtraction is: {subtract(num1, num2)}")
# #     elif choice == 3:
# #         print(f"The result of multiplication is: {multiply(num1, num2)}")
# #     elif choice == 4:
# #         print(f"The result of division is: {divide(num1, num2)}")
# #     else:
# #         print("Invalid choice!")

# # # Run the main function
# # if __name__ == "__main__":
# #     main()

def largest_number(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3 and n2>n1:
        return n2
    elif n3>n1 and n3>n2:
        return n3
    
n1=float(input("enter the first number"))
n2=float(input("enter the second number"))
n3=float(input("enter the third number"))

largest=largest_number(n1,n2,n3)

print(f"the largest number is {largest}")