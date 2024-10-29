import typing
class Solution:
    def solveNQueens(self, n: int) -> typing.List[typing.List[str]]:
        # Time: O(n!)
        # Space: O(n)
        # 1. Use a list to store the positions of the queens
        # 2. Use a set to store the columns that have been used
        # 3. Use a set to store the diagonals that have been used
        # 4. Use a set to store the anti-diagonals that have been used
        # 5. If we find a solution, then we add it to the result
        # 6. If we don't find a solution, then we backtrack
        # 7. If we have tried all the positions, then we return
        result = []
        self.dfs(n, [], set(), set(), set(), result)
        return result

    def dfs(self, n: int, queens: typing.List[int], columns: typing.Set[int], diagonals: typing.Set[int], anti_diagonals: typing.Set[int], result: typing.List[typing.List[str]]) -> None:
        row = len(queens)
        if row == n:
            result.append(self.print_result(queens))
            return
        for col in range(n):
            if col not in columns and row - col not in diagonals and row + col not in anti_diagonals:
                queens.append(col)
                columns.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                self.dfs(n, queens, columns, diagonals, anti_diagonals, result)
                queens.pop()
                columns.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
        return

    def print_result(self, queens: typing.List[int]) -> typing.List[str]:
        result = []
        for queen in queens:
            row = ['.'] * len(queens)
            row[queen] = 'Q'
            result.append(''.join(row))
        return result
    
if __name__ == "__main__":
    test = Solution()
    print(test.solveNQueens(4))
    print(test.solveNQueens(5))
    print(test.solveNQueens(6))
    print(test.solveNQueens(7))