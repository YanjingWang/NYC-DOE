class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False        
    
if __name__ == '__main__':
    s = Solution()
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print (s.searchMatrix([[1]], 1))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 0))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 51))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 10))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 20))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 16))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 1))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 50))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 7))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 34))
    print (s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 23))
        