import typing
class Solution:
    def getSkyline(self, buildings: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        """
        >>> Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
        [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        """
        if not buildings: return []
        if len(buildings) == 1: return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)
    
    def merge(self, left: typing.List[typing.List[int]], right: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        """
        >>> Solution().merge([[2,10],[3,15],[7,12],[12,0]],[[15,10],[20,8],[24,0]])
        [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        """
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                self.merge_helper(result, left[i])
                i += 1
            elif left[i][0] > right[j][0]:
                self.merge_helper(result, right[j])
                j += 1
            else:
                self.merge_helper(result, [left[i][0], max(left[i][1], right[j][1])])
                i += 1
                j += 1
        while i < len(left):
            self.merge_helper(result, left[i])
            i += 1
        while j < len(right):
            self.merge_helper(result, right[j])
            j += 1
        return result
    
    def merge_helper(self, result: typing.List[typing.List[int]], building: typing.List[int]) -> None:
        """
        >>> Solution().merge_helper([[2,10],[3,15],[7,12],[12,0]],[15,10])
        [[2,10],[3,15],[7,12],[12,0],[15,10]]
        """
        if not result:
            result.append(building)
            return
        if result[-1][1] == building[1]:
            return
        if result[-1][0] == building[0]:
            result[-1][1] = max(result[-1][1], building[1])
            return
        if result[-1][1] < building[1]:
            result.append(building)
            return
        if result[-1][1] > building[1]:
            if result[-1][0] < building[0]:
                result.append([building[0], result[-1][1]])
            result.append([building[0], building[1]])
            return
        
if __name__ == "__main__":
    test = Solution()
    print(test.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(test.getSkyline([[0,2,3],[2,5,3]]))
    print(test.getSkyline([[1,2,1],[1,2,2],[1,2,3]]))