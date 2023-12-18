import random

attempts_list = []
attempts = 0

rand_number = random.randint(1, 10)

player_name = input("what's your name : ").capitalize()
print (f"Welcome to my game, {player_name} !")
player = input("You wanna play my guessing game ? ").lower()



while player == "yes":
    print("I have guessed a number between 1 - 10 ")
    while True:
        try:
            guess = int(input("Enter your guess : "))
            attempts += 1
            attempts_list.append(attempts)

            if (guess < 1 or guess > 10):
                raise ValueError("Please guess a number within the given range")


            if guess == rand_number:
                print(f"Nice!, You got it after {attempts} attempts")
                break
            elif guess > rand_number :
                print("The number is lower ! ")
            else:
                print("The number is higher ! ")
                
        
        except ValueError as err:
            print(err)

    player = input("Do you want to play again? (yes/no) ").lower()
    
print("Have a nice day ! ")
