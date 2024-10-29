import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
            
        heaters.sort()
        res = 0

        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            dist1 = dist2 = float('inf')
            if idx > 0:
                dist1 = house - heaters[idx-1]
            if idx < len(heaters):
                dist2 = heaters[idx] - house
            res = max(res, min(dist1, dist2))

        return res
    
if __name__ == "__main__":
    test = Solution()
    houses = [1,2,3,4]
    heaters = [1,4]
    print (test.findRadius(houses, heaters))