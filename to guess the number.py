import random
n = random.randint(1,10)
Guess = -1
while Guess != 0:
    Guess = int(input("Guess the Number:"))
    if Guess < n:
        print("it os smaller")
    elif Guess > n :
          print("it is larger")
    else:
         print("correct guess")
         