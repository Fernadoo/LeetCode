'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = -1
        for i in range(len(nums)):
            if nums[i] > i + 1:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                if nums[i] == 


# # Recommended solution
# class Solution:
#     def firstMissingPositive(self, nums):
#         ind = 0
#         n_l = len(nums)
#         if not n_l:
#             return 1
        
#         while ind < n_l:
#             if ind + 1 == nums[ind]:
#                 pass
#             elif nums[ind] < 1 or nums[ind] > n_l:
#                 nums[ind] = -1
#             elif nums[ind] <= ind:
#                 nums[nums[ind] - 1] = nums[ind]
#                 nums[ind] = -1
#             else:
#                 t = nums[nums[ind] - 1]
#                 nums[nums[ind] - 1] = nums[ind]
#                 nums[ind] = (-1 if t == nums[ind] else t)
#                 ind -= 1
#             ind += 1
        
#         for i in range(n_l):
#             if i + 1 != nums[i]:
#                 return i + 1
#         return nums[-1] + 1

sol = Solution()
nums = [7,8,9,11,12]
print(sol.firstMissingPositive(nums))








