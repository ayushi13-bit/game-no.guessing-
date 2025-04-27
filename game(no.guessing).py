import random

target = random.randint(1, 100)

while True:
    try:
        userChoice = int(input("Guess the number: "))  # Convert input to integer
        if userChoice == target:
            print("Success: Correct guess!")
            break
        elif userChoice < target:
            print("Your number was too small, take a bigger guess.")
        else:
            print("Your number is too big, take a smaller guess.")
    except ValueError:  # If input is not an integer, show an error message
        print("Please enter a valid number.")

print("----GAME OVER----")

