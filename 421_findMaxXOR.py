class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        # 1. build the trie
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # 2. find the max xor
        max_xor = 0
        for num in nums:
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if 1 - bit in node.children:
                    xor += (1 << i)
                    node = node.children[1 - bit]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, xor)

        return max_xor
    
class TrieNode(object):
    def __init__(self):
        self.children = {}

if __name__ == "__main__":
    test = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    print(test.findMaximumXOR(nums))
    