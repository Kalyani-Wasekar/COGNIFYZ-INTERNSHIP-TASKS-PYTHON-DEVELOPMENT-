print("Welcome to the Number Guessing Game! Try to guess the number between 1 and 100.")
import random
#Generate a random number between 1 and 100
secret_num = random.randint(1, 100)
attempts=0
while(True):
    #Get the input from the user 
    guess=int(input("Enter your guess:"))
    attempts += 1
    #Check if the guess is correct or not
    if(guess == secret_num):
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break
    elif(guess < secret_num):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


