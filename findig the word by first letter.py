Food = ['Burger','pizza','hotdog','manchurian','noodles','garlic bread',]
letter = input("Enter the letter:")
for x in Food:
    if x.startswith(letter):
        print(x)