class Solution():
    """
    @param n: an int
    @return: an int f(n)
    """

    def fibonacci_recursion(self, n):
        # write your code here
        if n == 1:
            return 0
        if n == 2:
            return 1

        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_iteration(self, n):
        if n < 1:
            return -1
        if n == 1:
            return 0
        first = 0
        second = 1
        cnt = 2
        while cnt < n:
            # put it behind 
            third = first + second
            first = second
            second = third
            cnt += 1

        return second


# f1 = Solution()
# print(f1.fibonacci_recursion(10))  # overtime o(2**n) using loop is faster

f1 = Solution()
print(f1.fibonacci_iteration(999))
