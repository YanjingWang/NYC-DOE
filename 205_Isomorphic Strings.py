class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    

if __name__ == "__main__":
    test = Solution()
    s = "egg"
    t = "add"
    print(test.isIsomorphic(s, t)) # True
    s = "foo"
    t = "bar"
    print(test.isIsomorphic(s, t)) # False