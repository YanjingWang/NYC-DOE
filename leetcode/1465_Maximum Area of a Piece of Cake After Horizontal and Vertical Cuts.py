class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """

        # add the edges of the cake as cuts
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])

        # sort the cuts
        horizontalCuts.sort()
        verticalCuts.sort()

        # find the maximum gap between consecution horizontal and vertical cuts
        max_h = max(horizontalCuts[i] - horizontalCuts[i-1] for i in range(1, len(horizontalCuts)))
        max_v = max(verticalCuts[i] - verticalCuts[i-1] for i in range(1, len(verticalCuts)))

        # return the maximum area
        return (max_h * max_v) % (10**9 + 7)
    
if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [1,2,4]
    verticalCuts = [1,3]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
    # Output: 4
    
    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
    # Output: 6
    
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
    # Output: 9
    
    h = 1000000000
    w = 1000000000
    horizontalCuts = [2]
    verticalCuts = [2]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
    # Output: 81
