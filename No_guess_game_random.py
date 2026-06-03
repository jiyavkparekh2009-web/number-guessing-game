import random

print("\n" + "=" * 40)
print("\nNumber Guessing Game")
print("\n" + "=" * 40)

secret_no = random.randint(1,100)
print("You will get only 3 attempts")
guessed_no = int(input(" Enter the number : "))

won = False
attempt = 1

while attempt < 3:


    if guessed_no > secret_no:
        print("Too high!")
        guessed_no = int(input(" Enter the number again : "))


    elif guessed_no < secret_no:
        print("Too Low!")
        guessed_no = int(input(" Enter the number again : "))

    elif guessed_no == secret_no:
        print("Congratulations! You guessed the correct number.")
        won = True
        break

    attempt += 1



if (attempt == 3 and won == False):

    if guessed_no > secret_no:
        print("Too high!")
    elif guessed_no < secret_no:
        print("Too Low!")

    print("You lost the game!")


print(f"Total Attempts: {attempt}")
