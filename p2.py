'''n=int(input("enter the number"))
fact=1
if n<0:
    print("the number is nagative")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
print(f"factorial of {n} is {fact}")

def area_of_circle(r):
    area=2*3.14*r*r
    print(f"area of circle{area}")
def main():
    area_of_circle(4)
if __name__=="__main__":
    main()

r=int(input("enter the radius"))    
def area_of_circle(r):
    area=2*3.14*r*r
    print(f"area of circle{area}")
def main():
    area_of_circle(r)
if __name__=="__main__":
    main()'''
    
def love():
    h=input("enter the name")
    r=input("enter the name")
    return h,r
def main():
    h,r=love()
    print(f"i love u {r}")
    print(f"do u love {h}")
if __name__=="__main__":
    main()    