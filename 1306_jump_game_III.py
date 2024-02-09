class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
            
        # 1. Initialize
        # 2. Loop
        # 3. Return

        # 1. Initialize
        stack = [start]
        visited = set()

        # 2. Loop
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            visited.add(idx)
            for i in [idx - arr[idx], idx + arr[idx]]:
                if 0 <= i < len(arr) and i not in visited:
                    stack.append(i)

        # 3. Return
        return False
    
if __name__ == "__main__":
    test = Solution()
    print (test.canReach([4,2,3,0,3,1,2], 5)) # True
    print (test.canReach([4,2,3,0,3,1,2], 0)) # True