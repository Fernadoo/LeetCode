'''
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        action = [(0,1), (1,0), (0,-1), (-1,0)]
        action_chosen, i, j = 0, 0, 0
        output = []
        while True:
            # print(matrix[i][j])
            output.append(matrix[i][j])
            matrix[i][j] = 'x'
            i_ = i + action[action_chosen][0]
            j_ = j + action[action_chosen][1]
            count = 4
            while i_ == m or j_ == n or matrix[i_][j_] == 'x':
                action_chosen = (action_chosen + 1) % 4
                i_ = i + action[action_chosen][0]
                j_ = j + action[action_chosen][1]
                count -= 1
                if count == 0:
                    return output
            i, j = i_, j_
            # print(i,j)
        return output

            

sol = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
# matrix = [
#     [1]
# ]
print(sol.spiralOrder(matrix))