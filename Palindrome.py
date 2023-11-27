class Solution:
    """
    @param s: the data stream
    @return the judgement stream
    """

    def getStream(self, s):
        # appearance of odd numbers < = 1
        if s is None:
            return []
        alphabet = [0] * 26
        print(alphabet)
        count = 0
        answer = []
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1  #
            print(alphabet)
            if alphabet[ord(s[i]) - ord('a')] % 2 == 1:
                count += 1
            else:
                count -= 1
            if count > 1:
                answer.append(0)
            else:
                answer.append(1)
        return answer

    # s3 = Solution()  # Solution takes no arguments
    # print(s3.getStream('abba'))

    def longestSemiAlternatingSubstring(self, s):
        # 'baaabbabbb'
        if s is None or len(s) == 0:
            return 0
        maxLen = 1
        left = 0
        count = 1
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                count += 1
                if count >= 3:
                    left = right - 1
                    count = 2
            else:
                count = 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen

    # s4 = Solution()  # Solution takes no arguments
    # print(s4.longestSemiAlternatingSubstring('baaabbabbb'))

    def reverseASCIIEncodedString(self, encodeString):
        # initialize variable
        ans = ""
        for i in range(len(encodeString) - 1, 0, -2):
            asciiNumber = int(encodeString[(i - 1):(i + 1)])
            ans += chr(asciiNumber)
        return ans
# s5 = Solution()  # Solution takes no arguments
# print(s5.reverseASCIIEncodedString('7976'))
# string is immutable, 'a' is an address, 'ab' is another string Java stringBuilder is mutable
# N(n), O(n)
    def numberOfOperation(self,s):
        length = len(s)
        change_cnt= 0
        for i in range (length//2):
            change_cnt += abs(ord(s[i])-ord(s[length-1-i]))
        return change_cnt
s1 = Solution()  # Solution takes no arguments
print(s1.numberOfOperation('abcde'))
