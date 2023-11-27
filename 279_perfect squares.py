import math
from queue import Queue
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        perfect_squares = []
        i = 1
        while i*i <= n:
            perfect_squares.append(i*i)
            i += 1
        
        cnt = 0
        que = Queue(maxsize=0)
        que.put(n)
        while not que.empty():
            cnt += 1
            size = que.qsize()
            for _ in range(size):
                cur = que.get()
                for ps in perfect_squares:
                    if cur == ps:
                        return cnt
                    elif cur < ps:
                        break
                    else:
                        que.put(cur-ps)
        return cnt
    
if __name__ == "__main__":
    test = Solution()
    print(test.numSquares(12)) # 3
    print(test.numSquares(13)) # 2
    print(test.numSquares(1)) # 1
    print(test.numSquares(2)) # 2
    print(test.numSquares(3)) # 3
    print(test.numSquares(4)) # 1