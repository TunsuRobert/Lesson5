import random
import requests

def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    exchange_rate = data['rates']['ILS']
    return exchange_rate

def get_guess_from_user():
    guess = float(input("Enter your guess for the value in ILS: "))
    return guess

def play(difficulty):
    total_value = random.randint(1, 100)
    exchange_rate = get_exchange_rate()
    correct_value = total_value * exchange_rate

    print(f"Guess the value in ILS for {total_value} USD")

    user_guess = get_guess_from_user()

    if round(user_guess, 2) == round(correct_value, 2):
        print("Congratulations! You won.")
        return True
    else:
        print("Sorry, you lost. Better luck next time.")
        return False

# Example usage:
difficulty = 3  # Set the difficulty level (1 to 5)
play(difficulty)
