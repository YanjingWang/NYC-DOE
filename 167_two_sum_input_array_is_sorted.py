import typing
class Solution:
    def twoSum(self, numbers: typing.List[int], target: int) -> typing.List[int]:
        # 1. two pointer
        # Time: O(n)
        # Space: O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left + 1, right + 1]
            elif tmp < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

        # 2. binary search
        # Time: O(nlogn)
        # Space: O(1)
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1, -1]

        # 3. hash table
        # Time: O(n)
        # Space: O(n)
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]] + 1, i + 1]
            else:
                dic[target - numbers[i]] = i
        return [-1, -1]
    
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target)) # [1, 2]
    numbers = [2,3,4]
    target = 6
    print(Solution().twoSum(numbers, target)) # [1, 3]