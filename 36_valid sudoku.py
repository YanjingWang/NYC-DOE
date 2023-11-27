class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sudoku = board
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == '.':
                    continue
                if not self.check(sudoku, i, j):
                    return False
        return True
    
    def check(self, sudoku, i, j):
        for k in range(9):
            if k != i and sudoku[k][j] == sudoku[i][j]:
                return False
            if k != j and sudoku[i][k] == sudoku[i][j]:
                return False
        for k in range(3):
            for l in range(3):
                if (i//3)*3+k != i and (j//3)*3+l != j and sudoku[(i//3)*3+k][(j//3)*3+l] == sudoku[i][j]:
                    return False
        return True
    
if __name__ == '__main__':
    sudoku = [[".",".",".",".","5",".",".","1","."],
              [".","4",".","3",".",".",".",".","."],
              [".",".",".",".",".","3",".",".","1"],
              ["8",".",".",".",".",".",".","2","."],
              [".",".","2",".","7",".",".",".","."],
              [".","1","5",".",".",".",".",".","."],
              [".",".",".",".",".","2",".",".","."],
              [".","2",".","9",".",".",".",".","."],
              [".",".","4",".",".",".",".",".","."]]
    print(Solution().isValidSudoku(sudoku))