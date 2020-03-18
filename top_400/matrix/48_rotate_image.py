'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify 
the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return []
        def swap(a, b):
            tmp = b
            b = a
            a = tmp
            return [a,b]
        size = len(matrix)
        # flip upside down
        if size%2 == 0:
            for i in range(size//2):
                for j in range(size):
                    matrix[size//2 - i - 1][j], matrix[size//2 + i][j] = swap(matrix[size//2 - i - 1][j], matrix[size//2 + i][j])
                print(matrix)
        elif size%2 != 0:
            for i in range(size//2):
                for j in range(size):
                    matrix[size//2 - i - 1][j], matrix[size//2 + i + 1][j] = swap(matrix[size//2 - i - 1][j], matrix[size//2 + i + 1][j])
                print(matrix)
        # transpose
        for i in range(size):
            for j in range(i,size):
                matrix[i][j], matrix[j][i] = swap(matrix[i][j], matrix[j][i])
        return matrix

# 4 8
# 3 6

# 8 4 | 3 6
# 6 3 | 4 8

# 3 4 | 3 4
# 6 8 | 6 8




sol = Solution()
# img = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
'''
ret = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
img = [
  [ 5, 1, 9],
  [ 2, 4, 8],
  [13, 3, 6],
]
'''
ret = [
  [13, 2, 5],
  [3, 4, 1],
  [6, 8, 9],
]
''' 
print(sol.rotate(img))