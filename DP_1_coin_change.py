"""
You have three types of coins: 2-cent, 5-cent, and 7-cent. You want to make change for n cents. n=27
How many min coins do you need? 5+5+5+5+7=27
1. Define subproblems
2. Guess part of solution
3. Relate subproblem solutions
4. Recurse and memoize or build DP table bottom-up
5. Solve original problem
What is the status? Array f[i] = min coins to make change for i cents, f[i][j] = min coins to make change for i cents using only the first j types of coins
last coin is ak, the sum of rest of the coins k-1 coins are 27-ak, the optimal solution for 27-ak is f[27-ak] which is min coins to make change for 27-ak cents
if we use ak, then the total number of coins is f[27-ak]+1, if ak is not used, then the total number of coins is f[27-ak]
f[27] = min(f[27-2]+1, f[27-5]+1, f[27-7]+1)
f[27-2] = min(f[27-2-2]+1, f[27-2-5]+1, f[27-2-7]+1)
f[27-5] = min(f[27-5-2]+1, f[27-5-5]+1, f[27-5-7]+1)
f[27-7] = min(f[27-7-2]+1, f[27-7-5]+1, f[27-7-7]+1)
recursive formula: f[i] = min(f[i-2]+1, f[i-5]+1, f[i-7]+1)
int f(int i) {
    if (i < 0) return INF;
    if (i == 0) return 0;
    if (memo[i] != -1) return memo[i];
    int ans = INF;
    ans = min(ans, f(i-2)+1);
    ans = min(ans, f(i-5)+1);
    ans = min(ans, f(i-7)+1);
    memo[i] = ans;
    return ans;
}

initial condition: f[0] = 0, f[i] = INF for all i > 0, f[-1] = f[-2] = f[1] = f[3] = INF
boundary condition: f[i] = min(f[i-2]+1, f[i-5]+1, f[i-7]+1)
f[0] = 0, f[1] = f[3] = INF, f[2] = 1, f[4] = 2,  f[5] = 1, f[6] = 3, f[7] = 1, f[8] = 4, f[9] = 2, f[10] = 2, f[11] = 4, f[12] = 3, f[13] = 5, f[14] = 2, f[15] = 3, f[16] = 5, f[17] = 3, f[18] = 6, f[19] = 4, f[20] = 4, f[21] = 6, f[22] = 4, f[23] = 6, f[24] = 5, f[25] = 3, f[26] = 5, f[27] = 5

every step we have 3 choices, so the time complexity is O(3^n) = 27^3 = 19683, there is no repeated subproblems compared with recursive solution
"""
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        f = [float('inf')] * (amount+1) # f[i] = min coins to make change for i cents, initial condition: f[0] = 0, f[i] = INF for all i > 0
        f[0] = 0
        # select last coin
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    f[i] = min(f[i], f[i-coin]+1)
        if f[amount] == float('inf'):
            return -1
        return f[amount]
    
if __name__ == "__main__":
    coins = [2, 5, 7]
    amount = 27
    print(Solution().coinChange(coins, amount)) # 5
    print(Solution().coinChange([2], 3)) # -1
    print(Solution().coinChange([1], 0)) # 0
    print(Solution().coinChange([1], 1)) # 1
    print(Solution().coinChange([1], 2)) # 2
    print(Solution().coinChange([1,2,5], 11)) # 3
    print(Solution().coinChange([2], 1)) # -1
    print(Solution().coinChange([1], 2)) # 2
    print(Solution().coinChange([186,419,83,408], 6249)) # 20
    print(Solution().coinChange([3,7,405,436], 8839)) # 25
    print(Solution().coinChange([1,3,5,7,9], 100)) # 13
    print(Solution().coinChange([2,3,5], 100)) # 20
    print(Solution().coinChange([2,3,5], 1000)) # 200
    print(Solution().coinChange([2,3,5], 10000)) # 2000
    print(Solution().coinChange([2,3,5], 100000)) # 20000
    print(Solution().coinChange([2,3,5], 1000000)) # 200000
    print(Solution().coinChange([2,3,5], 10000000)) # 2000000
    # print(Solution().coinChange([2,3,5], 100000000)) # 20000000
    # print(Solution().coinChange([2,3,5], 1000000000)) # 200000000
    # print(Solution().coinChange([2,3,5], 10000000000)) # 2000000000
    # print(Solution().coinChange([2,3,5], 100000000000)) # 20000000000
    # print(Solution().coinChange([2,3,5], 1000000000000)) # 200000000000