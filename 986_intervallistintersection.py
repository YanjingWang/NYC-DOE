class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
            
        def intersect(a, b):
            if a[1] < b[0] or b[1] < a[0]:
                return []
            return [max(a[0], b[0]), min(a[1], b[1])]

        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            tmp = intersect(firstList[i], secondList[j])
            if tmp:
                res.append(tmp)
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
    
if __name__ == '__main__':
    test = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(test.intervalIntersection(firstList, secondList))