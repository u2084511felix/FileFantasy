
import os
import sys
import random
import curses

class SnakeGame:
    def __init__(self):
        self.screen = curses.initscr()
        curses.curs_set(0)
        self.height, self.width = self.screen.getmaxyx()
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.keypad(1)
        self.window.timeout(100)

        self.snake_x = self.width // 4
        self.snake_y = self.height // 2
        self.snake = [
            [self.snake_y, self.snake_x],
            [self.snake_y, self.snake_x - 1],
            [self.snake_y, self.snake_x - 2]
        ]

        self.food = [self.height // 2, self.width // 2]
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)

        self.key = curses.KEY_RIGHT

        self.game_over = False
        self.score = 0

    def update(self):
        new_key = self.window.getch()
        self.key = self.key if new_key == -1 else new_key

        if self.snake[0][0] in [0, self.height] or self.snake[0][1] in [0, self.width] or self.snake[0] in self.snake[1:]:
            self.game_over = True
            return

        new_head = [self.snake[0][0], self.snake[0][1]]

        if self.key == curses.KEY_DOWN:
            new_head[0] += 1
        if self.key == curses.KEY_UP:
            new_head[0] -= 1
        if self.key == curses.KEY_LEFT:
            new_head[1] -= 1
        if self.key == curses.KEY_RIGHT:
            new_head[1] += 1

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.food = None
            while self.food is None:
                nf = [
                    random.randint(1, self.height - 1),
                    random.randint(1, self.width - 1)
                ]
                self.food = nf if nf not in self.snake else None
            self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
        else:
            tail = self.snake.pop()
            self.window.addch(tail[0], tail[1], ' ')

        self.window.addch(self.snake[0][0], self.snake[0][1], '#')

    def __del__(self):
        curses.endwin()
'''
This is the snake.py file, which contains the SnakeGame class and its methods for handling the game logic.'''