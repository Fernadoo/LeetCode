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

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            # print("in")
            return [nums, []]
        nums_no_last = nums[0:-1]
        nums_last = nums[-1]
        # print(nums_no_last)
        subset_no_last = self.subsets(nums_no_last)
        # print(subset_no_last)
        for i in range(len(subset_no_last)):
            subset_no_last.append(subset_no_last[i] + [nums_last])
        # print(subset_no_last)
        return subset_no_last


sol = Solution()
nums = [1]
print(len(sol.subsets(nums)))
print(sol.subsets(nums))