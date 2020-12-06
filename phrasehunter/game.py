from phrasehunter.phrase import Phrase

import random

PHRASES = ['Hello',
           'North',
           'Go Home',
           'Nice to Meet you',
           'Who are you']


# Create your Game class logic in here.
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.activephrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        return [Phrase(phrase) for phrase in PHRASES]
    
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        while True:
            user_guess = input("Enter a letter: ")
            if len(user_guess) == 1 and user_guess.isalpha():
                return user_guess.lower()
            else:
                print("Input must be a single letter a-z")

    def welcome(self):
        print("------------------------")
        print("Welcome to Phrase Hunter")
        print("------------------------")

    def game_over(self):
        if self.missed < 5:
            print("Congratulations you won the Game")
        else:
            print("Sorry you lost the Game")

    
    def start(self):
        self.welcome()

        self.activephrase.display(self.guesses)

        while self.missed < 5 and not self.activephrase.check_complete(self.guesses):
            user_guess = self.get_guess()
            print(f"You entered: {user_guess}") 
            self.guesses.append(user_guess)
            self.activephrase.display(self.guesses)

            if not self.activephrase.check_guess(user_guess):
                self.missed += 1
            print(f"Number missed: {self.missed}")
        
        self.game_over()


        


