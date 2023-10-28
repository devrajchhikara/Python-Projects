import math
import random

print("WELCOME TO THE NUMBER GUESSING GAME\n")

#taking lower bound and upper bound as input
lower = int(input("Enter lower bound:" ))
upper = int(input("Enter upper bound:" ))

#Algorithm used for minimum number of guessing is log2(upper bound - lower bound + 1)
print("You only have", round(math.log(upper - lower + 1, 2)), "chances to guess the integer")

#generating random integer in range provided by player
x = random.randint(lower, upper)

#initializing guess count
count = 0

while count<(round(math.log(upper - lower + 1, 2))):
    count += 1
    #taking guess input by player
    guess = int(input(f"\nEnter your guess no. {count}: "))

    #Conditions testing
    if guess == x:
        print(f"\nCongratulation you have guessed the right number {x}")
        #breaking while loop when guessed!
        break
    elif guess > x:
        print(f"\n{guess} is more than the number")
    elif guess < x:
        print(f"\nYour guess {guess} is smaller than the number")
    
#When guess count exceeds the chances and player still did not guessed it right!
if count >= round(math.log(upper - lower + 1, 2)) and guess != x:
    print(f"{x} is the correct answer")
    print("Better luck next time")