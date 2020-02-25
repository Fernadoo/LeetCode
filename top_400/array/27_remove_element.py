'''
Given an array nums and a value val, remove all instances of that 
value in-place and return the new length.

Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you 
leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two 
elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five 
elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    def removeElement(self, nums, val) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums) -1 :
            all_is_val = 1
            for k in range(i, len(nums)):
                if nums[k] != val:
                    all_is_val = 0
            repeat = 0
            if nums[i] == val:
                if nums[i] == nums[i+1]:
                    repeat = 1
                for j in range(i, len(nums)-1):
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
                print(nums)
            if repeat == 1:
                if all_is_val == 1:
                    i += 1
            else:
                i += 1 
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        return len(nums) - count


sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))