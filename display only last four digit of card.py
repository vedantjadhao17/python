# while entering the card number give space between 4 digits
Card_Number =input("Enter card Number")
Last_digits = Card_Number[15::]
Four = '*'*4+' '
Display_Number = Four*3 + Last_digits
print(Display_Number)