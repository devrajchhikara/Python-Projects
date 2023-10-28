import random
from collections import Counter

#creating a string of fruits
words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
#splitting words string
words = words.split(' ')

#picking random fruit name
pick = random.choice(words)

if __name__=="__main__":
    
    print("-----Guess the word-----\n(hint: word is a name of fruit)")
    print()
    #printing empty spaces for letter in pick
    for i in pick:
        print("_", end=' ')
    
    #storing letter guessed by the player
    guessed = ''
    chances = len(pick) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0 and flag == 0: #flag updates when the word is correct
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("ENTER ONLY A LETTER")
            
            #Validation of the guess
            if not guess.isalpha():
                print("Enter only a letter")
                continue
            elif len(guess) > 1:
                print("Enter only a single letter")
                continue
            elif guess in guessed:
                print(f"You have already guessed letter {guess}")



            #if letter guessed is correct
            if guess in pick:
                
                k = pick.count(guess)   #k stores the no. of times letter guessed occurs in out picked word
                for j in range(k):
                    guessed += guess   #guessed letter is added as many times as it occurs in pick
                
            #print the word
            for char in pick:
                if char in guessed and (Counter(guessed) != Counter(pick)):
                    print(char, end=' ')
                    correct +=1

                #when player guessed all letters and it is correct
                elif Counter(guessed) == Counter(pick):
                    print(f"The word is {pick}")
                    flag = 1
                    print("Congratulations, You Won!")
                    break
                else:
                    print("_", end = ' ')

        #If player used all chances and still not able to guess all letters      
        if chances == 0 and Counter(guessed) != Counter(pick):
            print()
            print("You Lost! Try Again")
            print("The word was {}".format(pick))

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()