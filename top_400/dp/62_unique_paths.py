'''
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the 
grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
'''
import numpy as np

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = np.array([[0 for i in range(m)] for j in range(n)])
        grid[0, :] = 1
        grid[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[j, i] = grid[j-1, i] + grid[j, i-1]
        print(grid)
        return grid[n-1, m-1]

sol = Solution()
m, n = [7,3]
print(sol.uniquePaths(m, n))
