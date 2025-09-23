"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
print("=== SIMPLE GUESSING GAME ===")
random_number = random.randint(1, 10)
print("Guess my number between 1 and 20!")
print("You have 6 attempts.\n")
for i in range(1,7):
    guess_number = int(input(f"Attempt {i}/6 - Enter your guess: "))
    if guess_number == random_number:
        print(f"Congratulations! You won in {i} attempts!")
        break
    elif i==6 :
        print("Sorry your loss.\n")
    elif guess_number < random_number:
        print("Too low! Try again.\n")
    else:
        print("Too high! Try again.\n")