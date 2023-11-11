import random

if __name__ == "__main__":

    print("***Welcome to Rock - Paper - Scissor game***\n\nRules for the game are as follows:\n\n1)Rock vs Paper >> Paper wins\n2)Rock vs Scissor >> Rock wins\n3)Paper vs Scissor >> Scissor wins\n& vice versa")
    print("\nMake your choice\n1 >> Rock\n2 >> Paper\n3 >> Scissor")
    
    while True:
        choice = int(input("Enter your choice >> "))

        while (1 > choice) or (choice > 3):
            choice = int(input("Please enter a valid input again >> "))

        if choice == 1:
            choice_name = "rock"
        elif choice == 2:
            choice_name = "paper"
        elif choice == 3:
            choice_name = "scissor"

        print(f"\nUSER CHOICE :: {choice_name}")

        comp_choice = random.randint(1,3)

        if comp_choice == 1:
            comp_choice_name = "rock"
        elif comp_choice == 2:
            comp_choice_name = "paper"
        elif comp_choice == 3:
            comp_choice_name = "scissor"

        print(f"COMPUTER CHOICE :: {comp_choice_name}\n")
        
        if choice == comp_choice:
            print("This is a draw")
            result = "draw"

        if choice == 2 and comp_choice == 1:
            print("Paper wins", end = "")
            result = "paper"
        elif choice == 1 and comp_choice == 2:
            print("Paper wins", end = "")
            result = "PAPER"
        
        elif choice == 2 and comp_choice == 3:
            print("Scissor wins", end = "")
            result = "scissor"
        elif choice == 3 and comp_choice == 2:
            print("Scissor wins", end = "")
            result = "SCISSOR"

        elif choice == 1 and comp_choice == 3:
            print("Rock wins", end = "")
            result = "rock"
        elif choice == 3 and comp_choice == 1:
            print("Rock wins", end = "")
            result = "ROCK"

        if result == choice_name:
            print("--YOU WON--")
        elif result == "draw":
            print("****")
        else:
            print("---COMPUTER WINS---\n")

        PLAY = input("Do you want to play again? Y/N :- ")
        
        if PLAY.lower() == "y":
            print("RESTARTING GAME-------------------------->>\n")
            continue
        else:
            print("Quitting game :)")
            break
