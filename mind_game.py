
import random
def guessing_game():
    print("🎮 Welcome to the Guessing Game! ")
    secret_number = random.randint(1, 100)
    print(f"🤫 (Secret Number: {secret_number})")

    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("❌ Please enter a valid number!")
            continue

        guess = int(guess)

        # Check if number is within range
        if guess < 1 or guess > 100:
            print("🚫 Number should be between 1 and 100! Try again.")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts. 🎉")
            break

guessing_game()
