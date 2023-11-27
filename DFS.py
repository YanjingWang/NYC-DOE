# recursion is used to implement DFS
# the graph is represented by adjacency list
# the graph is undirected
# the graph is connected
# the graph is unweighted
# the graph is acyclic
# the graph is not necessarily a tree

#recursion calls itself, everytime it passes a different parameter when being called untill it reaches the exit and return all the way back to the first call
#iteration: for loop and while loop

def fibonacci(n):
    if n < 1 :  #base case: exit condition
        return -1
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
"""
def __init__(self):: This is the constructor of the Fibonaci class. It gets called when you create a new instance of this class.

self.cache = {}: This line initializes an empty dictionary that will be used to store previously calculated Fibonacci numbers. The reason for this is to avoid repeated calculation of the same Fibonacci numbers, which can slow down the program significantly for large inputs. This technique is known as memoization.
"""
class Fibonaci:
    def __init__(self):
        self.cache = {}
    def fibonacci(self, n):
        if n < 1 :
            return -1
        if n == 1 :
            return 0
        if n == 2 :
            return 1
        #memorization to avoid repeated calculation
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fibonacci(n-1)+self.fibonacci(n-2)
        return self.cache[n]
input = Fibonaci()
print(input.fibonacci(10))

def fibonacci(n):
    if n < 1 :
        return -1
    if n == 1 :
        return 0
    #memorization to avoid repeated calculation
    arr = [0 for _ in range(n+1)]
    arr[1] = 0
    arr[2] = 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci(n,arr):
    if n==1 or n==2 or arr[n]>0:
        return arr[n]
    arr[n] = fibonacci(n-1,arr)+fibonacci(n-2,arr)
    return arr[n]