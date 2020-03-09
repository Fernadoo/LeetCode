'''
Given a string, find the first non-repeating character 
in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in range(len(s)):
            try:
                tmp = d[s[i]]
                if tmp != 99999:
                    d[s[i]] = 99999
            except:
                d[s[i]] = i
        # print(d)
        min_index = min(list(d.values()))
        if min_index == 99999:
            return -1
        else:
            return min_index

sol = Solution()
s = "leetcode"
print(sol.firstUniqChar(s))
        