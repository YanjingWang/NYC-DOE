import random
class Solution:
    def bubbleSort(self, nums: [int]) -> [int]:
        # 第 i 趟「冒泡」
        for i in range(len(nums) - 1): # 对前 n 个元素进行 n 趟遍历
            flag = False    # 是否发生交换的标志位
            # 从数组中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
            for j in range(len(nums) - i - 1): # 每趟遍历都会确定一个最大值 # 对前 n - i 个元素进行遍历
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
                    print("第", i + 1, "趟，第", j + 1, "次交换：", nums)
            if not flag:    # 此趟遍历未交换任何元素，直接跳出
                break
        
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)
    
if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Before sorting:", nums)
    solution = Solution()
    print("After sorting:", solution.sortArray(nums))


# Space complexity: O(1) because we only use a constant amount of extra space to store the temp variable like flag, j, and i.
# Time complexity: O(n^2) because we have two nested loops. The outer loop runs n times, and the inner loop runs n - 1 times in the worst case.
# The total number of comparisons is n * (n - 1) / 2, which is O(n^2). The total number of swaps is also O(n^2). Why / 2? Because we compare two elements at a time.
