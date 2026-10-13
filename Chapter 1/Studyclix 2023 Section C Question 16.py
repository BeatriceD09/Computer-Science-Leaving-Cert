#(i.)
from random import randint

def guess_game(max_guesses_allowed):
    
    secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    print(max_guesses_allowed)
    if guess_count > max_guesses_allowed:
        print("Sorry, your out of guesses")
#(iii.) does not allow the user more than the maximum number of guesses
    while (user_guess != secret_number) and (guess_count < max_guesses_allowed):
        
#(iv.) asking the user for the maximum number of guesses allowed
        user_guess = int(input("Enter maximum number of guesses allowed: "))
        guess_count += 1     #Increase guess_count by 1
        if user_guess == secret_number:
                         print("Congratulations! You Win!")
                         
#(ii.) promt to hint the user
        elif user_guess > secret_number:
            print("Sorry, your guess if too high!")
            
        else:
            print("Sorry, your guess is too low!")
            
        
    print("You took", guess_count , "number of guesses")    #Shows the user the amount of guesses taken
                         
print("Welcome to the guessing game!")

user_max_guesses = int(input("Enter your guess: "))

guess_game(user_max_guesses)
