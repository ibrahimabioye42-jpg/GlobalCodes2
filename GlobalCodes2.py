import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
        elif guess < secret_number:
            print("📈 Too low! Try again.")
        elif guess > secret_number:
            print("📉 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts!")
            break

    except ValueError:
        print("❌ Please enter a valid number.")

print("Thanks for playing! 👋")

