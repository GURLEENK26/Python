# Guess the number program
# n=18 chuphana
# number of guesses is limited
# number of gueses left
# game over
# Number of guesses he take to win
print("------------------------------Guess the number---------------------------")
import random
num = random.randint(1,100)
noOfG = 1
print("Number of guesses is limited to only 7 times!!!\n")
while(noOfG <= 7):
    numByUser = int(input("Guess the number:\n"))
    if numByUser > num:
        print("You entered greater number please enter smaller number.\n")
    elif numByUser < num:
        print("You entered smaller number please enter greater number.\n")
    else:
        print("Hurray!! .. You won")
        print(noOfG, "no. of guesses he took to finish.")
        break
    print(7-noOfG, "no. of guesses left!\n")
    noOfG = noOfG+1
if noOfG>7:
     print("Game Over")
