"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bull & Cows - hra postavená na hádání 4 ciferného čísla

author: Zuzana Rulfová

email: rulfova.zuzana@gmail.com

discord: zuzana576

"""


import random
import time

def generate_unique_4_digit_number():
    """Generate a random 4-digit unique number."""
    digits = list(range(10))  # Create a list of digits from 0 to 9
    random.shuffle(digits)   # Shuffle the digits
    # Ensure the first digit is not 0 to avoid leading zeros
    if digits[0] == 0:
        digits[0] = random.choice(range(1, 10))
    # Take the first four shuffled digits to form the 4-digit number
    number = ''.join(map(str, digits[:4]))
    return number
    
def count_bulls_and_cows(secret_number, guess):
    """Count the number of bulls and cows in a guess."""
    bulls = 0
    cows = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows
    
def is_valid_guess(guess):
    """
    Checks if the guess is a valid 4-digit number without repetition of digits.
    """
    # Ensure the input is a number with 4 digits
    if not guess.isdigit() or len(guess) != 4:
        return False
    # Ensure the number is without repetition of digits
    if len(set(guess)) != 4:
        return False
    # Ensure the first digit is not 0 to avoid leading zeros
    if int(guess[0]) == 0:
        return False
    return True

def main():
    secret_number = generate_unique_4_digit_number()

    division_line = "-" * 57
    print("Hi there!")
    print(division_line)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print(division_line)
    start_time = time.time()
    
    print("Enter a number: ")
    print(division_line)
    

    attempts = 0
    while True:
        guess = input(">>> ")
        if not is_valid_guess(guess):
            print("Invalid input.")
            print("Please enter a valid 4-digit number without repetition of digits and without 0 as the first digit.")
            print(division_line)
            continue

        bulls, cows = count_bulls_and_cows(secret_number, guess)
        if bulls < 2:
            bulls_text = "bull"
        else:
            bulls_text = "bulls"
        if cows < 2:
            cows_text = "cow"
        else:
            cows_text = "cows"
        if bulls < 4:
            print(f"{bulls} {bulls_text}, {cows} {cows_text}")
            print(division_line)
        
        attempts += 1
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Time taken: {elapsed_time:.2f} seconds")
            break

if __name__ == "__main__":
    main()
