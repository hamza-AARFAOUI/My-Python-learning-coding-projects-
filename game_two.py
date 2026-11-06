import random

def guess_the_number():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Take a guess: ")
        attempts += 1

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < number_to_guess:
            print("Too low! Try again   maybe u can add .")
        elif user_guess > number_to_guess:
            print("Too high! Try again maybe u can SUB .")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.  GOOD JOB")
            break


guess_the_number()