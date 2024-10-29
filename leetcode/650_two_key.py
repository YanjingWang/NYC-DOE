class Solution:
    def minSteps(self, n: int) -> int:
        dp_array = [0] * (n+1)
        for i in range(2,n+1):
            dp_array[i] = i
            for j in range(i-1,1,-1):
                # if (i-j) % j ==0:
                #     dp_array[i] = dp_array[j] + 1 + (i-j) % j
                if i % j == 0:
                    dp_array[i] = dp_array[j] + (i//j)
                    break
        return dp_array[n]
 
#testing 
s = Solution()
print(s.minSteps(3))


s2 = Solution()
print(s2.minSteps(1))

s2 = Solution()
print(s2.minSteps(4))