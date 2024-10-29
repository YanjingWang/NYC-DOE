class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
            
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c for c in word)
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}
        
        for word in wordlist:
            words_cap.setdefault(word.lower(), word)
            words_vow.setdefault(devowel(word.lower()), word)
        
        def solve(query):
            if query in words_perfect:
                return query
            if query.lower() in words_cap:
                return words_cap[query.lower()]
            if devowel(query.lower()) in words_vow:
                return words_vow[devowel(query.lower())]
            return ""
        
        return map(solve, queries)

if __name__ == '__main__':
    sol = Solution()
    print (sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
    print (sol.spellchecker(["yellow"], ["YellOw"]))
    print (sol.spellchecker(["yellow"], ["yellow"]))
    print (sol.spellchecker(["yellow"], ["YELLow"]))