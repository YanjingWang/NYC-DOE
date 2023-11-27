class Solution():
    """
    @param s: a string
    @return: whether the string is a valid parentheses
    stack: LIFO
    """

    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            # push in stack
            if ch == '{' or ch == '[' or ch == '(':  #left paratheses need to be appended
                stack.append(ch)
            else: #right paratheses need to be checked
                if not stack: 
                    # stack is empty, no left paratheses to match
                    return False
                if ch == ']' and stack[-1] != '[' or ch == '}' and stack[-1] == '{' or ch == ')' and stack[-1] != '(':
                    return False

                # pop the stack if the paratheses are matched
                stack.pop()
        return not stack  # if stack is empty return True, else return False

if __name__ == '__main__':
    input = Solution()
    #input.isValidParentheses('(){}[]') #True
    #input.isValidParentheses('(}[{') #False
    print(input.isValidParentheses('{[]}()')) #True 
