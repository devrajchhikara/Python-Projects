#Bagram / Twenty plus one / 21 number game / drinking game
#This game goal is to make other player say/count 21
""" 
Rules for the game:
1) Count numbers consecutively after other player's turn otherwise you will lose.
2) You can only count upto 3 numbers together in each turn.
3) The player who calls “21” is eliminated.

>>Your oppenent here is Computer (player 2)
(Hint: you can only win in second chance with counting upto multiple of 4)
"""

#finding next multiple of 4 from giving number
def NearestMultiple4(num):
    if num >= 4:
        near = num + (4 - (num%4))
    else:
        near = 4
    return near

#when player loses
def lose():
    print("\n\nYou Lose!\nBetter Luck next time")
    exit(0)

#Checking if entered values are consecutive
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i += 1
    return True

#starts the game
def start():
    #for storing both players inputs
    xyz = []
    last = 0
    while True:
        #asking to choose turn
        print("Enter F to take first chance.\nEnter S to take second chance.")
        chance = input(">> ")

        #Turn 1
        if chance.upper() == "F":
            while True:
                if last == 20: #if last == 20(by computer), next count will be obviously 21 and the player loses
                    lose()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you want to enter?")
                    inp = int(input(">> "))

                #Validating input & calculating number of inputs to be given by computer
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game")
                        lose()

                    i, j = 1, 1      #i for player & j for computer
                
                print("Enter the values -")
                #taking input of numbers
                while i<= inp:
                    a = int(input(">> "))
                    xyz.append(a)
                    i += 1

                #storing last number
                last = xyz[-1]

                #Validating input (consecutive condition)
                if check(xyz) == True:
                    if last == 21:
                        lose()
                    
                    #Computer inputs and storing last value
                    else:
                        while j <= comp:
                            xyz.append(last + j)
                            j += 1
                        print("Order of inputs after computer's turn is: {}".format(xyz))
                        last = xyz[-1]
                
                else:
                    print("You did not entered consecutive numbers")
                    lose()

        #Turn 2      
        elif chance.upper() == "S":
            #initializing computer's turn
            comp = 1

            while last < 20:
                #first input by computer will be 1 after that taking consecutive no. of inputs after player's turn accordingly.
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                
                print("Order of inputs after Computer's turn is: {}".format(xyz))
                #Losing condition
                if xyz[-1] == 20:
                    lose()
                #Continue
                else:
                    print("Your turn\nHow many numbers do you want to enter?")
                    inp = int(input(">> "))
                    
                    #Validating input value
                    if inp > 0 and inp <= 3:
                        i = 1
                        print("Enter your values.")
                        while i <= inp:
                            a = int(input(">> "))
                            xyz.append(a)
                            i += 1
                        #updating last
                        last = xyz[-1]
                        
                        if check(xyz) == True:
                            #calculating next comp value
                            near = NearestMultiple4(last)
                            comp = near - last
                            if comp == 4:
                                comp = 3
                            else:
                                comp = comp
                        
                        else:
                            print("You did not entered consecutive numbers")
                            lose()
                    #invalid input (not in range 0<inp<=3)
                    else:
                        print("Invalid numbers")
                        lose()
            #Winning condition when it's computer turn to count 21
            print("Congratulations, You won!")
            exit(0)
        
        else:
            print("Wrong choice!")


game = True
#Game interface
while game == True:
    print("Player 2 is computer")
    print("Do you want to play the 21 number game? (YES / NO)")
    ans = input(">> ").upper()
    if ans == "YES" or ans == "Y":
        start()
    else:
        print("Do you want to exit this game? (Y/N)")
        ex = input(">> ").upper()

        if ex == "Y":
            print("Quitting the game")
            exit(0)
        elif ex == "N":
            print("Continuing...")
        else:
            print("Wrong choice")