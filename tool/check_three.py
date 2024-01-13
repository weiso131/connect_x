import numpy as np
from check_win import continue_n


def check_three(board : list, row : int, col : int, choice : int, player : int):
    pass



test_empty = [[
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0,
]]
print(continue_n(test_empty, 6, 7, 2, 1, 3))
