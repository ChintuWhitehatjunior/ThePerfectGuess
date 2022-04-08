from logging import exception
import random
randNo = random.randint(1,100)
ans = None
guess = 0
try:
    while(ans != randNo):
        ans = int(input("Enter your guess:- "))          
        if(ans == randNo):
            guess += 1
            print("You Guessed Right!")
            if(guess>1):
                print(f"It took you a single guess, Amazing!")
            else:
                print(f"It took you {guess} guesses")

        elif(ans > randNo):
                print("Enter a lower no and try again")
                guess += 1
        else:
                print("Enter a higher no and try again")
                guess += 1
except Exception as e:
    print(f"Your input caused an error, please input an integer and try again!")
