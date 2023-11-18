#Guessing Game
import random
from random import randint

while True:
    
    rdm = randint(1, 100)
    print("\nCorrect Number:", rdm, "\n")

    try:
        
        guess = int(input("Enter your guess:"))
        if guess == rdm:
            print("Correct!")
            ask = str(input("\nWould you like to play again?:"))
            if ask == "yes":
                continue
            else:
                print("Goodbye!!!")
                break

        else:
            print("Incorrect!")
            guess

    except ValueError:
         print("Invalid Integer")