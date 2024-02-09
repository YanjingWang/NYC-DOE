class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
            
        def replace(word, dictionary):
            for i in range(1, len(word)):
                if word[:i] in dictionary:
                    return word[:i]
            return word

        return " ".join([replace(word, dictionary) for word in sentence.split()])
    
if __name__ == "__main__":
    print(Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
    print(Solution().replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
    print(Solution().replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
    print(Solution().replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery"))
    print(Solution().replaceWords(["ac","ab"], "it is abnormal that this solution is accepted"))
    