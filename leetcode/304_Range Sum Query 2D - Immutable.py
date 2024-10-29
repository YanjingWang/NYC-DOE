import typing
class NumMatrix:

    def __init__(self, matrix: typing.List[typing.List[int]]):
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+matrix[i-1][j-1]
        print(self.dp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.dp[row2+1][col2+1], self.dp[row2+1][col1], self.dp[row1][col2+1], self.dp[row1][col1])
        return self.dp[row2+1][col2+1]-self.dp[row2+1][col1]-self.dp[row1][col2+1]+self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#test code
if __name__ == "__main__":
    test = NumMatrix([[3, 0, 1, 4, 2], 
                        [5, 6, 3, 2, 1],
                        [1, 2, 0, 1, 5],
                        [4, 1, 0, 1, 7],
                        [1, 0, 3, 0, 5]])
    print(test.sumRegion(2, 1, 4, 3)) # 8
    print(test.sumRegion(1, 1, 2, 2)) # 11
    print(test.sumRegion(1, 2, 2, 4)) # 12
    print(test.sumRegion(0, 0, 0, 0)) # 3