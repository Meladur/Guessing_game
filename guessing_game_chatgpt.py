import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        min_attempts = max(attempts_list)
        print(f"The current high score is {min_attempts} attempts")

player_name = input("What's your name: ").capitalize()
print(f"Welcome to my game, {player_name}!")

player = input("Do you want to play my guessing game? ").lower()

while player == "yes":
    rand_number = random.randint(1, 10)  # Move inside the loop
    attempts = 0  # Reset attempts for each game
    show_score()
    print("I have guessed a number between 1 - 10 ")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            attempts_list.append(attempts)

            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range")

            if guess == rand_number:
                print(f"Nice! You got it after {attempts} attempts")
                break
            elif guess > rand_number:
                print("The number is lower!")
            else:
                print("The number is higher!")

        except ValueError as err:
            print(err)

    player = input("Do you want to play again? (yes/no) ").lower()

print("Have a nice day!")
