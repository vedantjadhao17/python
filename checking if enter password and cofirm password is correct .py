pass1 = input("Enter password:")
pass2 =input("Cofirm password:")
if pass1 == pass2:
    print("Matched")
elif pass1.casefold() == pass2.casefold():  
    print("Please check for the cases and try again")
else:
     print("They are not matchig")