class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
            
        # check if it is possible to make m bouquets with k flowers in each bouquet
        def check(x):
            bouquets = flowers = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= x:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets == m:
                    return True
            return False

        if len(bloomDay) < m * k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
    

if __name__ == "__main__":
    bloomDay = [1,10,3,10,2]
    m = 3
    k = 1
    print(Solution().minDays(bloomDay, m, k))
    print(f"Correct Answer is: 3")