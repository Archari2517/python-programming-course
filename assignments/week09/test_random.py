import random

def test_random():
    random_number = random.randint(1, 10)
    print("== Get number between 1-10 ==")
    guess_number = int(input("Enter your guess number :"))
    if guess_number == random_number:
        print(f"Congratulation The number is {random_number}")

    elif guess_number < random_number:
        print("Too low.")
        print(f"The number is {random_number}")
    else:
        print("Too high.")
        print(f"The number is {random_number}")
    
test_random()