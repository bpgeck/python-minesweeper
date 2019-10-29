import argparse
import fileinput

from data_board import Data_Board
from display_board import Display_Board

'''
Product requirements:
* Square board of size N
* Number of mines M
* Mines randomly distributed
* If you choose a mine, game over
* If you choose a space next to a mine, space becomes the number of mines next to it
* If you choose a space with 0 mines next to it perform a "flood"
* A "flood" auto selects all spaces bordering the 0 mines space over and over until you hit a numbered spot
'''
def main():
    parser = argparse.ArgumentParser(description='Getting the board size, and number of mines.')
    parser.add_argument('-b', action='store', dest='board_size', type=int, required=True,
                        help='Set the width and height size of the minesweeper board (board is a square)')
    parser.add_argument('-n', action='store', dest='num_mines', type=int, required=True,
                        help='Set the number of mines present in the board (randomly distributed)')

    args = parser.parse_args()

    if (args.num_mines > args.board_size * args.board_size):
        print ("ERROR: You've requested too many mines")
        return

    data_board = Data_Board(args.board_size, args.num_mines)
    display_board = Display_Board(data_board)

    display_board.show()
    while True:
        row = int(input("Row: "))
        col = int(input("Column: "))

        game_status = display_board.pick_space(row, col)
        display_board.show()

        if game_status == "WIN":
            print("You Win!")
            break
        elif game_status == "LOSE":
            print("You Lose :(")
            break

if __name__ == "__main__":
    main()