import numpy as np

from data_board import Data_Board

class Display_Board:
    def __init__(self, data_board):
        if not isinstance(data_board, Data_Board):
            raise Exception("data_board param must be of type Data_Board")
        
        self.data_board = data_board
        self.board_size = data_board.board_size
        self.num_mines = data_board.num_mines

        self.display_board = np.chararray(data_board.board.shape, unicode=True)
        self.display_board[:] = '.'

        self.explored_spaces = []

    def pick_space(self, row, col):
        if row < 0 or row >= self.board_size:
            print("Invalid value specified for row. Must be in the range [0, " + str(self.board_size - 1) + "]")
            return "CONTINUE"
        if col < 0 or col >= self.board_size:
            print("Invalid value specified for col. Must be in the range [0, " + str(self.board_size - 1) + "]")
            return "CONTINUE"

        space_data = self.data_board.get_space(row, col)

        if space_data[0] == "EMPTY" and space_data[1] == 0:
            flooded_spaces = self.flood(row, col)
            for flooded_space in flooded_spaces:
                self.explored_spaces.append((flooded_space[0][0], flooded_space[0][1]))
                self.display_board[flooded_space[0][0]][flooded_space[0][1]] = flooded_space[1][1]
        elif space_data[0] == "BOMB":
            self.display_board[row][col] = 'B'
            return "LOSE"
        else:
            self.explored_spaces.append((row, col))
            self.display_board[row][col] = space_data[1]

        if len(self.explored_spaces) == self.board_size * self.board_size - self.num_mines:
            return "WIN"
        else:
            return "CONTINUE"

    '''
    Perform an exhasutive graph search expanding from the provided row, col
    Graph possible "next" nodes are the neighboring spaces on the board (including diagonal spaces)
    Expand the node if the number of neighboring bombs is 0

    Returns a list of nodes that were visited during the flood. An element of this list of formatted like so:
    ((row, col), ("BOMB" or "EMPTY", num_adjacent_bombs)), ((),()), etc.
    '''
    def flood(self, row, col):
        stack = [(row, col)]
        visited = set()
        flooded_spaces = []

        max_iterations = 10
        while len(stack) > 0:
            (cur_row, cur_col) = stack.pop()

            # Don't need to investigate a node we already visited
            if (cur_row, cur_col) not in visited:
                space_data = self.data_board.get_space(cur_row, cur_col)

                # Only continue filling if there are no bordering mines
                if space_data[0] == "EMPTY" and space_data[1] == 0:
                    neighbors = self.data_board.get_neighboring_spaces(cur_row, cur_col)
                    for neighbor in neighbors:

                        # Don't add a neighbor that has already been visited
                        if neighbor not in visited:
                            stack.append(neighbor)

                visited.add((cur_row, cur_col))
                flooded_spaces.append(((cur_row, cur_col), space_data))

        return flooded_spaces

    def show(self):
        print(self.display_board)