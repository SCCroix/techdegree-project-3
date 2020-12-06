# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop




if __name__ == "__main__":
    continue_game = True
    while continue_game:

        game = Game()
        print(game.activephrase.phrase)
        game.start()

        continue_game_input = ""
        while continue_game_input not in ["y", "n"]:
            continue_game_input = input("Play again (y/n)").lower()
            
        continue_game = continue_game_input == "y"

        


