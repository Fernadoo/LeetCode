import numpy as np
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < - 2**31 or x > 2**31 -1:
            return 0
        ptr = len(str(abs(x))) - 1
        ret = ""
        start = 0
        while ptr >= 0:
            if start == 0 and str(abs(x))[ptr] == "0":
                ptr -= 1
            else: 
                start = 1
                ret += str(abs(x))[ptr]
                print(ret)
                ptr -= 1
        if ret == "":
            return 0
        else:
            ret = np.sign(x) * eval(ret)
            if ret < - 2**31 or ret > 2**31 -1:
                return 0 
            return ret

# # Recommended solution
# # pop operation:
# pop = x % 10;
# x /= 10;

# # push operation:
# temp = rev * 10 + pop;
# rev = temp;

sol = Solution()
x = 1534236469
print(sol.reverse(x))