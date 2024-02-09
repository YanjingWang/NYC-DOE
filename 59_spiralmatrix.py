class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 1. simulation
        # O(n^2)
        matrix = [[0] * n for _ in range(n)]
        seen = [[False] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(n*n):
            matrix[r][c] = i + 1
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return matrix
    
        # # 2. layer by layer
        # # O(n^2)
        # matrix = [[0] * n for _ in range(n)]
        # left, right, top, bottom, num = 0, n-1, 0, n-1, 1
        # while left <= right and top <= bottom:
        #     for c in range(left, right+1):
        #         matrix[top][c] = num
        #         num += 1
        #     for r in range(top+1, bottom+1):
        #         matrix[r][right] = num
        #         num += 1
        #     if left < right and top < bottom:
        #         for c in range(right-1, left, -1):
        #             matrix[bottom][c] = num
        #             num += 1
        #         for r in range(bottom, top, -1):
        #             matrix[r][left] = num
        #             num += 1
        #     left, right, top, bottom = left+1, right-1, top+1, bottom-1
        # return matrix
    
        # # 3. spiral
        # # O(n^2)
        # matrix = [[0] * n for _ in range(n)]
        # dr = [0, 1, 0, -1]
        # dc = [1, 0, -1, 0]
        # r = c = di = 0
        # for i in range(n*n):
        #     matrix[r][c] = i + 1
        #     cr, cc = r + dr[di], c + dc[di]
        #     if 0 <= cr < n and 0 <= cc < n and matrix[cr][cc] == 0:
        #         r, c = cr, cc
        #     else:
        #         di = (di + 1) % 4
        #         r, c = r + dr[di], c + dc[di]
        # return matrix
    
if __name__ == "__main__":
    n = 3
    print(Solution().generateMatrix(n)) # [[1,2,3],[8,9,4],[7,6,5]]