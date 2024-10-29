import random
class Solution:
    def shellSort(self, nums: [int]) -> [int]:
        size = len(nums)
        gap = size // 2
        # 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序数组第 1 个元素
                temp = nums[i]
                j = i
                # 从右至左遍历每组中的有序数组元素
                while j >= gap and nums[j - gap] > temp: # 逆序时，交换符号即可
                    # 将每组有序数组中插入位置右侧的元素依次在组中右移一位
                    nums[j] = nums[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                nums[j] = temp
                print('gap:', gap, '第', i, '趟，插入', temp, '：', nums)
            # 缩小 gap 间隔
            gap = gap // 2
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.shellSort(nums)
    
if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(10)]
    print('Before sorting:', nums)
    solution = Solution()
    print('After sorting:', solution.sortArray(nums))
