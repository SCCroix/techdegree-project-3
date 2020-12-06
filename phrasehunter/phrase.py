# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                output = letter
            else:
                output = "_"
            print(f"{output}", end=" ")
        print()

    def check_guess(self, guess):
        return (guess in self.phrase)

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True