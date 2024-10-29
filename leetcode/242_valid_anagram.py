class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('rat', 'car'))