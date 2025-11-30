# Number Guessing Game
import random

def main():
    print("Welcome to Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have unlimited tries. Type 'exit' to quit.\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (1-100): ").strip()
        if guess.lower() == "exit":
            print("You quit. The number was:", secret)
            break

        if not guess.isdigit():
            print("Please type a valid number or 'exit'.")
            continue

        guess_num = int(guess)
        attempts += 1

        if guess_num < 1 or guess_num > 100:
            print("Guess must be between 1 and 100.")
            continue

        if guess_num == secret:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess_num < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    main()
     
