"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1]]
        for i in range(1, numRows):
            new = [1 for j in range(i + 1)]
            for k in range(1, i):
                new[k] = dp[i - 1][k - 1] + dp[i - 1][k]
            dp.append(new)
        return dp


sol = Solution()
num = 12
print(sol.generate(num))