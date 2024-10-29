class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # # Solution 1: TLE
        # from collections import defaultdict

        # edges = defaultdict(int)
        # for row in wall:
        #     sum = 0
        #     for brick in row[:-1]:  # Skip the last brick
        #         sum += brick
        #         edges[sum] += 1

        # max_edges = max(edges.values(), default=0)
        # return len(wall) - max_edges
    
        # Solution 2: Accepted
        """
        The path that cuts through the minimum number of bricks is the path that passes through the most brick edges/endpoints.
        We can keep a map where we count where each brick ends as a distance from the left-most point (i.e. from 0).
        We build this map on a per-row basis, as we want to find out where each brick ends, and how many times each brick ends on the same point.
        We also want to ignore the right-most brick's endpoint, since both the left-most and right-most edges of the wall are ignored as solutions.
        The solution is the number of rows of bricks (i.e. len(wall)) minus the maximum of the number of rows you can avoid by cutting through a certain brickEndpoint.
        """
        brickEndpointsToCount = {}
        
        for bricks in wall:
			# Initialise brickEndpoint to 0, i.e. the left-most point of the wall.
            brickEndpoint = 0
            
			# Ignore the very last brick for each row since their endpoints are always the right-most part of the wall.
            for i in range(len(bricks) - 1):
                brick = bricks[i]
				# Update the brickEndpoint by adding the length of the current brick in the row.
                brickEndpoint += brick
                
				# We've seen this endpoint before, so increment the count.
                if brickEndpoint in brickEndpointsToCount:
                    brickEndpointsToCount[brickEndpoint] += 1
				# This brickEndpoint hasn't been seen before, so initialise the count to 1.
                else:
                    brickEndpointsToCount[brickEndpoint] = 1
        
		# Use this assignment to shorten the ternary operator in the return statement.
        counts = brickEndpointsToCount.values()        
    
    

if __name__ == '__main__':
    test = Solution()
    print(test.leastBricks([[1,2,2,1],
                            [3,1,2],
                            [1,3,2],
                            [2,4],
                            [3,1,2],
                            [1,3,1,1]]))
    print(test.leastBricks([[1],[1],[1]]))