import random

def guess_the_number():
    print("- Hello! What is your name?")
    name = input()
    print(f"- Well, {name}, I am thinking of a number between 1 and 20.")
    thinking_number = random.randint(1, 20)
    chances = 0
    while True:
        
        print("- Take a guess.")
        guess = int(input())

        chances += 1

        if guess < thinking_number:
            print("- Your guess is too low.")
        elif guess > thinking_number:
            print("- Your guess is too high.")
        else:
            print(f"- Good job, {name}! You guessed my number in {chances} guesses!")
            break

guess_the_number()
