
# Version1

CORRECT_NUMBER = 26

user_guess = int(input("What is your guess? "))

if user_guess == CORRECT_NUMBER:
    print("Wow, you got it - great guessing!")
else:
    print("Sorry, Your guess is incorrect")
    

# Version2

CORRECT_NUMBER = 26

while True:
    user_guess = int(input("What is your guess? "))

    if user_guess == CORRECT_NUMBER:
        print("Wow, you got it - great guessing!")
        break
    else:
        print("Sorry, Your guess is incorrect")
        
        
# Version3

import random

LOWER_BOUND = 1
UPPER_BOUND = 100
GUESS_LIMIT = 5
GUESS_COUNTER = 0
CORRECT_NUMBER = random.randint(LOWER_BOUND, UPPER_BOUND)


print(f"Try guessing the number that I'm thinking. It is between {LOWER_BOUND} and {UPPER_BOUND}. Good luck, you have {GUESS_LIMIT} guesses!")


while True:
    user_guess = int(input("What is your guess? "))
    GUESS_COUNTER += 1
    remaining_guesses = GUESS_LIMIT - GUESS_COUNTER
    
    if LOWER_BOUND <= user_guess <= UPPER_BOUND:
        
        if user_guess == CORRECT_NUMBER:
            print(f"Wow, you got it in { GUESS_COUNTER} guesses - well done!")
            break
        elif user_guess < CORRECT_NUMBER:
            print(f"Your guess is too low, try again! Guessing remaining: {remaining_guesses}")   
        else:
            print(f"Your guess is too high, try again! Guessing remaining: {remaining_guesses}")
            
    else:
        print(f"Your guess is outside the range, try a guess between {LOWER_BOUND} and {UPPER_BOUND}. guesses remaining: {remaining_guesses}  ")
    
    if remaining_guesses == 0:
        print(f"Sorry you're out of guesses, The number you were after was {CORRECT_NUMBER}")
        break





























