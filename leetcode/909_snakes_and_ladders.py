from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        def get(s):
            #given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col
        
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            s, step = queue.popleft()
            for s2 in range(s+1,min(s+7,n*n+1)):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 == n*n:
                    return step + 1
                if s2 not in visited:
                    visited.add(s2)
                    queue.append((s2, step + 1))
        return -1
    
if __name__ == "__main__":
    test = Solution()
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    
    print(test.snakesAndLadders(board))
    # Output: 4