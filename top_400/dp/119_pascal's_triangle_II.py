"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""

from copy import deepcopy


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [0 for i in range(rowIndex + 1)]
        prev_dp = [0 for i in range(rowIndex + 1)]
        dp[0] = 1
        prev_dp[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(1, i + 1):
                dp[j] = prev_dp[j - 1] + prev_dp[j]
            prev_dp = deepcopy(dp)
        return prev_dp


sol = Solution()
rowIndex = 4
print(sol.getRow(rowIndex))
