class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
            
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
    
if __name__ == "__main__":
    test = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print (test.dailyTemperatures(temperatures))