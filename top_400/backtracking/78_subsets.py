'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# # Recursive
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) == 0:
#             return []
#         if len(nums) == 1:
#             # print("in")
#             return [nums, []]
#         # print(nums_no_last)
#         ret = self.subsets(nums[:-1])
#         # print(subset_no_last)
#         for i in range(len(ret)):
#             ret.append(ret[i] + [nums[-1]])
#         # print(subset_no_last)
#         return ret

# # Iterative
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ret = [[]]
#         for i in range(len(nums)):
#             for j in range(len(ret)):
#                 ret.append(ret[j] + [nums[i]])
#         return ret

# Backracking
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


sol = Solution()
nums = [1, 2, 3]
print(len(sol.subsets(nums)))
print(sol.subsets(nums))