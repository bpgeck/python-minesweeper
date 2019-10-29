import numpy as np

class Data_Board:
    def __init__(self, board_size, num_mines):
        self.board_size = board_size
        self.num_mines = num_mines

        self.board = np.concatenate((np.ones(num_mines), np.zeros(board_size * board_size - num_mines)))
        np.random.shuffle(self.board)
        self.board.shape = (board_size, board_size)

    def get_space(self, row, col):
        if row < 0 or row >= self.board_size:
            raise Exception("Invalid value specified for row. Must be in the range [0, " + (self.board_size - 1) + "]")
        if col < 0 or col >= self.board_size:
            raise Exception("Invalid value specified for col. Must be in the range [0, " + (self.board_size - 1) + "]")

        if self.board[row][col] == 1:
            return ("BOMB", 0)
        else:
            neighbors = self.get_neighboring_spaces(row, col)
            bomb_count = sum([self.board[neighbor[0]][neighbor[1]] for neighbor in neighbors])
            return ("EMPTY", int(bomb_count))

    def get_neighboring_spaces(self, row, col):
        neighbors = []

        # top-left
        if row-1 >= 0 and col-1 >= 0:
            neighbors.append((row-1, col-1))
        
        # top-center
        if row-1 >= 0:
            neighbors.append((row-1, col))
        
        # top-right
        if row-1 >= 0 and col+1 < self.board_size:
            neighbors.append((row-1, col+1))
        
        # center-left
        if col-1 >= 0:
            neighbors.append((row, col-1))

        # center-right
        if col+1 < self.board_size:
            neighbors.append((row, col+1))

        # bottom-left
        if row+1 < self.board_size and col-1 >= 0:
            neighbors.append((row+1, col-1))

        # bottom-center
        if row+1 < self.board_size:
            neighbors.append((row+1, col))

        # bottom-right
        if row+1 < self.board_size and col+1 < self.board_size:
            neighbors.append((row+1, col+1))

        return neighbors