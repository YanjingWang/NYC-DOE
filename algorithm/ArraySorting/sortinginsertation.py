import random 
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
                print("第", i, "趟，第", j, "次移动：", nums)
            # 将该元素插入到适当位置
            nums[j] = temp
            print("第", i, "趟，插入", temp, "：", nums)

        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.insertionSort(nums)
    
if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(10)]
    print('Before sorting:', nums)
    solution = Solution()
    print('After sorting:', solution.sortArray(nums))
