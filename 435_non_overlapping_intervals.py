import typing
class Solution:
    def eraseOverlapIntervals(self, intervals: typing.List[typing.List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        # 1. Sort the intervals by the end time
        # 2. Iterate through the intervals
        # 3. If the start time of the current interval is less than the end time of the previous interval, then we have an overlap
        # 4. Otherwise, we can update the previous interval to the current interval
        # 5. Return the number of overlaps
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev[1]:
                count += 1
            else:
                prev = curr
        return count
    
if __name__ == "__main__":
    test = Solution()
    print(test.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(test.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(test.eraseOverlapIntervals([[1,2],[2,3]]))
    print(test.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))