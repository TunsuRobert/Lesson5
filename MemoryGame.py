import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101)
            for _ in range(difficulty)]

def get_list_from_user(difficulty):
    user_sequence = []
    for _ in range(difficulty):
        number = int(input("Enter a number: "))
        user_sequence.append(number)
    return user_sequence

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    print("Memory Game Starting...")
    secret_sequence = generate_sequence(difficulty)
    print("Memorize the sequence for 0.7 seconds...")
    time.sleep(0.7)  # Pause for 0.7 seconds
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(secret_sequence, user_sequence):
        print("Congratulations! You won.")
        return True
    else:
        print("Sorry, you lost. Better luck next time.")
        return False

# Example usage:
difficulty = 5  # Change the difficulty as needed
play(difficulty)
