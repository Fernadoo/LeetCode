'''
Given a positive integer n, find the least number of perfect 
square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import math
import sys

# # TLE
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         dp = [sys.maxsize] * (n + 1)
#         dp[0] = 0
#         max_i = round(math.sqrt(n))
#         for i in range(1, max_i+1):
#             for j in range(0, n+1 - i**2):
#                 dp[j + i**2] = min(dp[j + i**2], dp[j] + 1)
#         # print(dp)
#         return dp[n]


# not TLE
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        max_i = math.floor(math.sqrt(n))
        l = [i**2 for i in range(1, max_i+1)]
        for i in l:
            for j in range(0, n+1 - i):
                dp[j + i] = min(dp[j + i], dp[j] + 1)
        # print(dp)
        return dp[n]


sol = Solution()
n = 13
print(sol.numSquares(n))

