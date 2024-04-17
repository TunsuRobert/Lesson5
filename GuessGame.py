import random

secret_number = None
difficult = None

def generate_number():
    global secret_number, difficult
    difficult = int(input("Difficulty: "))
    random_number = random.randint(1, difficult)
    secret_number = random_number

def get_guess_from_user():
    global difficult
    guess = int(input(f"Insert a number between 1 and {difficult}: "))
    return guess

def compare_result():
    global secret_number, difficult
    while True:
        guess = get_guess_from_user()
        if guess == secret_number:
            print("You guessed the number")
            break
        else:
            print("Try again")




def play():
    generate_number()
    return compare_result()
play()