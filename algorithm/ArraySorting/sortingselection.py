import random 
class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        for i in range(len(nums) - 1):
            # 记录未排序区间中最小值的位置
            min_i = i
            print('i:', i)
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
                    print('min_i:', min_i)
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
                print('第', i + 1, '趟，交换：', nums)
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.selectionSort(nums)

if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(10)]
    print('Before sort:', nums)
    solution = Solution()
    print('After sort:', solution.sortArray(nums))