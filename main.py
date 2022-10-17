# Number Guessing Game
from art import number_guess_logo
import random
easy_turn = 10
hard_turn = 5
def check_answer(guess, number, turns):
    if guess > number:
        print("Too High.")
        return turns-1
    elif guess < number:
        print("Too Low.")
        return turns-1
    else:
        print(f"The actual number is : {number}")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_turn
    elif level == 'hard':
        return hard_turn
'''turns = 10
game_not_end = True
while game_not_end:
    guess = int(input("Guess a number: "))
    if turns == 0:
        game_not_end = False'''
def game():
    print(number_guess_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randrange(1, 100)
    print(f"Pssst, the correct answer is {number}")
    turns = difficulty()
    guess = 0
    while guess!= number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
game()