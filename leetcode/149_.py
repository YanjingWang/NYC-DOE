import typing
class Solution:
    def maxPoints(self, points: typing.List[typing.List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 2
        for i in range(len(points)-1):
            slope = {}
            same_points = 0
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same_points += 1
                elif points[i][0] == points[j][0]:
                    slope["inf"] = slope.get("inf", 0) + 1
                else:
                    slope[(points[j][1]-points[i][1])/(points[j][0]-points[i][0])] = slope.get((points[j][1]-points[i][1])/(points[j][0]-points[i][0]), 0) + 1
            max_points = max(max_points, max(slope.values())+same_points+1)
        return max_points
    
if __name__ == "__main__":
    test = Solution()
    points = [[1,1],[2,2],[3,3]]
    print(test.maxPoints(points)) # 3
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(test.maxPoints(points)) # 4