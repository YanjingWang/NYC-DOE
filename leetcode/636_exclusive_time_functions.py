class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
            
        # 1. Initialize
        # 2. Loop
        # 3. Return

        # 1. Initialize
        stack = []
        res = [0] * n
        prev_time = 0

        # 2. Loop
        for log in logs:
            id, type, time = log.split(':')
            id, time = int(id), int(time)
            if type == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        # 3. Return
        return res
    
if __name__ == "__main__":
    print (Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])) # [3, 4]
    print (Solution().exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])) # [8]
    print (Solution().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])) # [7, 1]
    print (Solution().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"])) # [8, 1]

