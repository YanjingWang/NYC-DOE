class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
            
        # if intervals is empty, return newInterval
        if not intervals:
            return [newInterval]
        
        # if newInterval is empty, return intervals
        if not newInterval:
            return intervals
        
        # if newInterval is not empty, insert it into intervals
        intervals.append(newInterval)
        
        # sort intervals by the first element of each interval
        intervals.sort(key=lambda x: x[0])
        
        # initialize a list to store the merged intervals
        merged = []
        
        # for each interval in intervals
        for interval in intervals:
            
            # if merged is empty or the last interval in merged does not overlap with the current interval
            if not merged or merged[-1][1] < interval[0]:
                
                # append the current interval to merged
                merged.append(interval)
                
            # if the last interval in merged overlaps with the current interval
            else:
                
                # merge the last interval in merged with the current interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
# Time complexity: O(nlogn) to sort intervals
# Space complexity: O(n) to store the merged intervals
# where n is the number of intervals in intervals
if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,5],[6,9]]
    
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,2],[3,10],[12,16]]
    
    intervals = []
    newInterval = [5,7]
    print(Solution().insert(intervals, newInterval))
    # Output: [[5,7]]
    
    intervals = [[1,5]]
    newInterval = []
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,5]]
    
    intervals = [[1,5]]
    newInterval = [2,3]
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,5]]
    
    intervals = [[1,5]]
    newInterval = [2,7]
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,7]]
    
    intervals = [[1,5]]
    newInterval = [6,8]
    print(Solution().insert(intervals, newInterval))
    # Output: [[1,5],[6,8]]
    
    intervals = [[1,5]]
    newInterval = [0,3]
    print(Solution().insert(intervals, newInterval))
    # Output: [[0,5]]
    
    intervals = [[1,5]]
    newInterval = [0,0]
    print(Solution().insert(intervals, newInterval))
    # Output: [[0,0],[1,5]]
    
    intervals = [[1,5]]
    newInterval = [0,6]
    print(Solution().insert(intervals, newInterval))
    # Output: [[0,6]]
    
    intervals = [[1,5]]
    newInterval = [0,7]
    print(Solution().insert(intervals, newInterval))
    # Output: [[0,7]]
    
    intervals = [[1,5]]
    newInterval = [0,8]
    print(Solution().insert(intervals, newInterval))
    # Output
