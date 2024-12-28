'''person=input("whats your name")
person'''
year=int(input("enter the year"))
while True:
    
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"{year}is a leap yeaar")
            else:
                print(f"{year}is not a leap year")
        else:
            print(f"{year}is a leap year")
    else:
        print(f"{year}is not leap year")

'''# Program to find leap years using a while loop

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Start year and end year
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# Variable to track the current year
current_year = start_year

# Using a while loop to find leap years
while current_year <= end_year:
    if is_leap_year(current_year):
        print(f"{current_year} is a leap year.")
    current_year += 1  # Move to the next year'''

