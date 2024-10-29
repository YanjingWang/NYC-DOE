class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """

        # Time: O(n)
        # Space: O(n)
        if indexDiff <= 0 or valueDiff < 0:
            return False
        # bucket sort
        buckets = {}
        for i, num in enumerate(nums):
            bucket = num // (valueDiff + 1)
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            buckets[bucket] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        return False