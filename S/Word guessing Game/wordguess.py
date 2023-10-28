import random

#words list
words = ['hello','rainbow','bat','sun','animal','slow','black','car','water','space']

#picking random word from word list
pick = random.choice(words)
turns = 12

#Welcome player
name = input("Enter your Name: ")
print("--------------GUESS THE WORD GAME--------------")
print(f"Good luck {name}, you have only {turns} turns to guess the word")

#empty string to store guessed characters
char_guessed = ''

#condition
while turns > 0:

    #taking input for character guessed by player
    guess = input("Guess a character : ")
    #storing guess in char_guessed
    char_guessed += guess
    
    failed = 0
    #condition for display characters
    for char in pick:
        if char in char_guessed:
            print(char)
        else:
            print("_")
            failed += 1

    #winning condition
    if failed == 0:
        print(f"YOU WON, {pick} is the right word")
        break
    
    #leftover turns
    if guess not in pick:
        turns -= 1
        print('Wrong')
        print("You have" , turns, "more guesses")

        if turns == 0:
            print("You lose")