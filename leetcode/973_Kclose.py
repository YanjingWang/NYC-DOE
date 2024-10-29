import heapq, random
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
            
        # 1. sort
        # O(nlogn)
        # points.sort(key=lambda P: P[0]**2 + P[1]**2)
        # return points[:k]
        
        # 2. heap
        # O(nlogk)
        # heap = []
        # for (x, y) in points:
        #     dist = -(x**2 + y**2)
        #     if len(heap) == k:
        #         heapq.heappushpop(heap, (dist, x, y))
        #     else:
        #         heapq.heappush(heap, (dist, x, y))
        # return [[x, y] for (dist, x, y) in heap]
        
        # 3. quick select
        # O(n)
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        
        def sort(i, j, k):
            if i >= j: return
            oi, oj = i, j
            pivot = dist(random.randint(i, j))
            while i < j:
                while i < j and dist(i) < pivot: i += 1
                while i < j and dist(j) > pivot: j -= 1
                points[i], points[j] = points[j], points[i]
            if k <= i - oi + 1:
                sort(oi, i, k)
            else:
                sort(i+1, oj, k - (i - oi + 1))
        
        sort(0, len(points) - 1, k)
        return points[:k]
    
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(Solution().kClosest(points, k)) # [[3,3],[-2,4]]