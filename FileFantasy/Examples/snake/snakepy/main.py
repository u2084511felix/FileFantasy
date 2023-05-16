
import sys
import time
import random
from snake import SnakeGame

def main():
    game = SnakeGame()

    while True:
        game.update()
        time.sleep(0.1)

        if game.game_over:
            print("Game Over! Your score: {}".format(game.score))
            break

if __name__ == "__main__":
    main()
    
'''
This is the main.py file, which initializes and runs the SnakeGame.'''