class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                else:
                    if i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
        

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid('{[]}'))
    print(s.isValid('(('))
    print(s.isValid('))'))
    print(s.isValid('(('))