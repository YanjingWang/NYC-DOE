class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        freq_list = []
        for key, value in freq_dict.items():
            freq_list.append((key, value))
        freq_list = sorted(freq_list, key=lambda x: x[1], reverse=True)
        return [freq_list[i][0] for i in range(k)]
    
# Path: 347_top_K_frequent_element.py
# Method: Bucket Sort
# Time Complexity: O(n)
# Space Complexity: O(n)
if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))
