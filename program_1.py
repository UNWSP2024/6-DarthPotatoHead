#Program Written By: Ainsley Bellamy
#Date Written: 02/27/2025
#Program Title: DiceRoll_Average


# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

#Function to generate two random numbers between 1-6 and calculate sum, return sum.
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    # Sum 2 numbers
    numSum = num1 + num2
    return numSum
    # return sum to calling function

#Mainline, under which the randDice() function runs 100 times adding the results to the empty
#list rollContainer so that the average can be calculated.
if __name__ == "__main__":
    def main():
        rollContainer = []
        for i in range(100):
            randDice()
            rollContainer.append(randDice())
#Calculate average and print.
        print(f"{sum(rollContainer) / 100:.2f}")