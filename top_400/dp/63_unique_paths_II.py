'''
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
import numpy as np

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        grid = np.array([[0 for i in range(m)] for j in range(n)])
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            grid[0, i] = 1
        for j in range(n):
            if obstacleGrid[j][0] == 1:
                break
            grid[j, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[j][i] == 1:
                    grid[j, i] = 0
                else:
                    grid[j, i] = grid[j-1, i] + grid[j, i-1]
        print(grid)
        return grid[n-1, m-1]

sol = Solution()
obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]
                        ]
print(sol.uniquePathsWithObstacles(obstacleGrid))
