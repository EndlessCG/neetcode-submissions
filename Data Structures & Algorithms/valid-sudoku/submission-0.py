import numpy as np
def no_dup(r):
    nums = [n for n in r if n != '.']
    # print(r, nums)
    return len(nums) == len(set(nums))
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        row_valid = all(no_dup(r) for r in board)
        col_valid = all(no_dup(board[:, i]) for i in range(9))
        grid_valid = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = board[i:i+3, j:j+3].flatten()
                if not no_dup(grid):
                    grid_valid = False
        # print(row_valid, col_valid, grid_valid)
        return row_valid and col_valid and grid_valid
        