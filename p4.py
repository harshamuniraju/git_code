'''a="harsha"
#b="asdf"
if a.isalnum:
    print("true")
else:
    print("false")

print(a>=b)
print(len(a))
print(a[3])
print(a[1:3])

def main():
    a=input("enter string")
    if a==a[::-1]:
        print("string is palandrom")
    else:
        print("is not palandrom")
if __name__=="__main__":
    main()

def main():
    user_string=input("enter the string")
    count_character=0
    for each_character in user_string:
        count_character +=1
    print(f"length of string {count_character}")
if __name__=="__main__":
    main()
    
list=[1,2,3,4,5]
print(2 in list)'''

ab="my name is"
dc=["harsha"]
bc=dc+list(ab)
print(bc)