class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
            
        # Sliding window
        # Time: O(k)
        # Space: O(1)
        n = len(cardPoints)
        window_size = n - k
        min_sum = float('inf')
        curr_sum = 0
        for i in range(n):
            curr_sum += cardPoints[i]
            if i >= window_size:
                curr_sum -= cardPoints[i - window_size]
            if i >= window_size - 1:
                min_sum = min(min_sum, curr_sum)
        return sum(cardPoints) - min_sum
    
if __name__ == "__main__":
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints, k))