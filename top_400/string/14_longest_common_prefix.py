'''
Write a function to find the longest common 
prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        min_lens = min([len(s) for s in strs])
        ret = ""
        stop = 0
        for i in range(min_lens):
            for s in strs:
                if s[i] != strs[0][i]:
                    return ret
            ret += s[i]
        return ret

sol = Solution()
strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))
