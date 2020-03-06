'''
You are given coins of different denominations and a total 
amount of money amount. Write a function to compute the fewest 
number of coins that you need to make up that amount. If 
that amount of money cannot be made up by any combination 
of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
'''
import copy

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [9999 for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:

            for i in range(0, amount+1-coin):
                dp[i+coin] = min(dp[i]+1, dp[i+coin])
            # print(coin, dp, dp_last) 
        if dp[amount] == 9999:
        	return -1
        else:
        	return dp[amount]

sol = Solution()
coins = [1,3,5]
amount = 8
print(sol.coinChange(coins, amount))
