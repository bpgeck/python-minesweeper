Python Minesweeper Practice
===========

By Brendan Geck

A python command-line implementation of minesweeper

How to use:
-----------
Download the source files and unzip into the same directory

`cd` into the directory and run `pip install -r requirements.txt`

There are two command line arguments: `b <BOARD_SIZE>` and `-n <NUM_BOMBS>`
Begin the game by specifying both like so: `python minesweeper.py -b 4 -n 5`
This will start a game with a board 4 by 4 and 5 hidden mines

You will be prompted to enter a Row and Column. This is the spot you are "Clicking" to guess that no bomb is underneath.
If a bomb is underneath, you will lose and the program will end.
Continue selecting until you get all the correct spaces. You will be met with a "You Win!" and the program will end.