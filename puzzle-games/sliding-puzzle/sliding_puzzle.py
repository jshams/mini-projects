from collections import deque
from time import sleep


class Board:
    def __init__(self, board, zero_loc=None):
        # board is a 2d tuple representing the board
        self.board = self.list_to_tuple(board)
        # store the height of the board (int)
        self.height = len(board)
        # store the width of the board (int)
        self.width = len(board[0])
        # sore the zero location of the board as a tuple(int, int)
        # if it wasn't passed in find it
        self.zero_loc = zero_loc if zero_loc is not None else self.find_zero()

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
        return self.board == other.board

    def __iter__(self):
        '''generates coordinates and values at those coordinates'''
        for i in range(self.height):
            for j in range(self.width):
                yield (i, j), self.board[i][j]

    def tuple_to_list(self, tup):
        '''convert an n dimensional tuple to an n dim list recursively'''
        try:

            return [self.tuple_to_list(t) for t in tup]
        except TypeError:
            return tup

    def list_to_tuple(self, lst):
        '''convert an n dimensional list to an n dim tuple recursively'''
        try:
            if len(lst) == 0:
                return lst
            return tuple(self.list_to_tuple(l) for l in lst)
        except TypeError:
            return lst

    def swap(self, tile_loc, to_self=False):
        '''
        swap a tile with the zero
        if to_self is true, this board will be manipulated, otherwise, a new
        board will be returned
        '''
        # convert this board to a list to allow mutation
        list_b = self.tuple_to_list(self.board)
        # unpack the tile location to ti and tj
        t_i, t_j = tile_loc
        # unpack the zero location to zi and zj
        z_i, z_j = self.zero_loc
        # swap the values at these coordinates
        list_b[t_i][t_j], list_b[z_i][z_j] = list_b[z_i][z_j], list_b[t_i][t_j]

        # if to self is true change the board value of self
        if to_self:
            self.board = self.list_to_tuple(list_b)
            # change the zero loc to tile loc (they were just swapped)
            self.zero_loc = tile_loc
        # otherwise return a new board with this swap
        else:
            return Board(list_b, tile_loc)

    def find_zero(self):
        '''returns the zero location'''
        # iterate over self
        for coords, num in self:
            # when the tile num is 0
            if num == 0:
                # return the coords of that tile
                return coords

    def next_moves(self):
        '''generate next moves from this board'''
        i, j = self.zero_loc

        # up
        if i > 0:
            yield (i - 1, j)
        # down
        if i < self.height - 1:
            yield (i + 1, j)
        # left
        if j > 0:
            yield (i, j - 1)
        # right
        if j < self.width - 1:
            yield (i, j + 1)

    @property
    def is_solved(self):
        '''returns a boolean indicating whether this board is solved'''
        # check if the tile in the bottom right corner is 0
        # quick indicator that the board is not solved
        if self.board[-1][-1] != 0:
            return False
        # iterate over the tiles in self, while also iterating over values
        # that should correlate to tile nums
        for (coord, num), real_val in zip(self, range(1, self.width * self.height - 1)):
            # if the num is not equal to the real val the board is not solved
            if num != real_val:
                return False
        # once checks are done, return True
        return True


class Solver:
    def __init__(self, board):
        self.board = Board(board)
        self.seen = set([self.board])
        self.queue = deque()
        self.queue.append(self.board)
        self.solution = None

    def solve(self):
        '''solves the board using BFS. returns a tuple of moves'''
        while self.queue:
            # get the next board from the queue
            board = self.queue.popleft()
            # add the board to seen board
            self.seen.add(board)
            # perform a set of moves on the board
            solved_board = self.move(board)
            # check if any of those moves resulted in a solved board
            if solved_board is not None:
                # recursively backtrack through prev boards to get the solution
                self.solution = tuple(self._get_moves(solved_board))
                return self.solution

    def move(self, board):
        '''performs a set of new moves from one state and adds the new
        states to the queue so long as it hasnt been seen.
        Returns None if no solved board was found, otherwise return the solved
        board object'''
        # get the next moves from this board
        next_moves = board.next_moves()
        # iterate over the next moves
        for move in next_moves:
            # create a new board state by performing that move
            new_board = board.swap(move)
            # stpre the prev move and prev board in this new board
            new_board.prev_move = move
            new_board.prev_board = board
            # check if the board has not been seen
            if new_board not in self.seen:
                # check if the board is solved
                # first check if the move was to the bottom right corner
                if move == (board.width - 1, board.height - 1):
                    if new_board.is_solved:
                        # if the board is solved return it
                        return new_board
                self.queue.append(new_board)
        return None

    def _get_moves(self, board):
        '''generate moves from a solved board using recursive backtracking'''
        try:
            yield from self._get_moves(board.prev_board)
            prev_move = board.prev_move
            yield prev_move
        except AttributeError:
            pass

    def display_solution(self, sleep_len=0.5):
        '''prints the solution with fancy colors and dramatic pauses'''

        if self.solution is None:
            print('Solver:NotSolvedError: call self.solve before',
                  'displaying a solution')
            exit()
        board = self.board.swap((self.board.zero_loc))

        BLUE = '\033[94m'
        GREEN = '\033[92m'
        END = '\033[0m'
        RED = '\033[91m'

        print('Start:')
        for row in board.board:
            print(f'\t{row}')
        print()

        for itr, move in zip(range(1, len(self.solution) + 1), self.solution):
            sleep(sleep_len)
            print(
                f'Move {itr}: {BLUE}{board.zero_loc}{END} <-> {RED}{move}{END}')
            board_str = ''
            for i, row in enumerate(board.board):
                board_str += '\t('
                for j, col in enumerate(row):
                    if j != 0:
                        board_str += ', '
                    if board.zero_loc == (i, j):
                        board_str += f'{BLUE}{col}{END}'
                    elif move == (i, j):
                        board_str += f'{RED}{col}{END}'
                    else:
                        board_str += f'{col}'
                board_str += ')\n'
            board.swap(move, True)
            print(board_str)
        sleep(sleep_len)
        print(f'Done in {len(self.solution)} moves:{GREEN}')
        for row in board.board:
            print(f'\t{row}')
        print(END)


b = Board([[0, 2, 3], [1, 4, 6], [7, 5, 8]])

s = Solver(b.board)
solution = s.solve()
s.display_solution()


# 200522-83643
