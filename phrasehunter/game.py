from phrasehunter.phrase import Phrase

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
        self.activephrase = None
        self.guesses = [" "]

    def create_phrases(self):
        return [Phrase(phrase) for phrase in PHRASES]
    
