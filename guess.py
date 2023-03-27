import random

def main():
    print("This is a Number Guessing Game!")
    print("I am thinking of a number between 1 and 100, try and guess!")
    random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 & 100.")
        
        attempts += 1

        if user_guess < 1 or user_guess > 100:
            print("Number out of range. Your guess must be a number between 1 & 100.")
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number}")
            break
        elif user_guess > secret_number:
            print("Your guess is too high! Please try again.")
        else:
            print("Your guess is too low! Please try agian.")
        
if __name__ == "__main__":
    main()