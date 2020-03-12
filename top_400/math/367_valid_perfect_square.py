'''
Given a positive integer num, write a function which returns 
True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        while True:
            if i ** 2 == num:
                return True
            elif i ** 2 > num:
                return False
            i += 1


# Newton's method
# Explanation -- https://en.wikipedia.org/wiki/Newton%27s_method.
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

sol = Solution()
num = 16
print(sol.isPerfectSquare(num))