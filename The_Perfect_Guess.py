import random
randNo = random.randint(1,100)
ans = None
guess = 0
while(ans != randNo):
    ans = int(input("Enter your guess:- "))          
    if(ans == randNo):
        guess += 1
        print("You Guessed Right!")
        print(f"It took you {guess} guess/guesses")
    else:
        if(ans > randNo):
            print("Enter a lower no and try again")
            guess += 1
        else:
            print("Enter a higher no and try again")
            guess += 1




    
