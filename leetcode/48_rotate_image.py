import typing
class Solution:
    def rotate(self, matrix: typing.List[typing.List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. reverse
        for i in range(len(matrix)):
            matrix[i].reverse()

if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    test.rotate(matrix)
    print(matrix) # [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    test.rotate(matrix)
    print(matrix) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    matrix = [[1]]
    test.rotate(matrix) # [[1]]