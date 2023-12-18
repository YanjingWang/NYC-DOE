class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
            
        def flip(arr, k):
            i, j = 0, k - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        def find(arr, target):
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
        
        res = []
        for i in range(len(arr), 0, -1):
            idx = find(arr, i)
            if idx == i - 1:
                continue
            elif idx == 0:
                res.append(i)
                flip(arr, i)
            else:
                res.append(idx + 1)
                flip(arr, idx + 1)
                res.append(i)
                flip(arr, i)
        return res
    
if __name__ == "__main__":
    arr = [3,2,4,1]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: [4,2,4,3]")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")
    
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
    print(f"Correct Answer is: []")