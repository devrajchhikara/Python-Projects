import random

#picking random 4 digit number
pick = random.randrange(1000,10000)
#taking player's guess
num = int(input("Enter your 4 digit number : "))

#if player is able to guess in first chance
if pick == num:
    print("Congratulations! You are a MASTERMIND.\n{} is the right guess".format(num))

else:
    #count for no. of chances used
    chance = 0

    #loop to take inputs until right guess
    while num != pick:

        numstr = str(num)
        pickstr = str(pick)
        correct = ["X"]*4
        count = 0

        #for display of correct digits guessed!
        for i in range(4):
            if numstr[i] == pickstr[i]:
                count += 1
                correct[i] = pickstr[i]
        
            else:
                continue

        print(f"\nYou guessed {count} right digits of numbers")
        print(correct)
        print()

        #taking guess input again 
        num = int(input("Enter your next guess value of number: "))
        
        chance += 1

    #when player is able to guess the right answer
    if num == pick:
        print(f"{pick} is the correct answer!!!")
        print(f"You have become a Mastermind. It took {chance} turns to guess the number")