import typing
class Solution:
    def countBits(self, n: int) -> typing.List[int]:
        """
        >>> Solution().countBits(2)
        [0, 1, 1]
        >>> Solution().countBits(5)
        [0, 1, 1, 2, 1, 2]
        """
        result = [0]
        for i in range(1, n+1):
            result.append(result[i//2] + i%2)
        return result
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    test = Solution()
    print(test.countBits(5))
    print(test.countBits(2))
