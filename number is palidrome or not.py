a=int(input("Enter the number:"))
m=a
rev=0
while a>0:
    r = a%10
    a = a//10
    rev = rev*10+r
if m == rev:
        print("Number is palidrome")
else:
            print("Number is not palidrome")
    