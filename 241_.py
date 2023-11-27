import typing
class Solution:
    def diffWaysToCompute(self, expression: str) -> typing.List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
# test code
s = Solution()
print(s.diffWaysToCompute("2-1-1"))
print(s.diffWaysToCompute("2*3-4*5"))
print(s.diffWaysToCompute("2"))
print(s.diffWaysToCompute("2+3"))   

