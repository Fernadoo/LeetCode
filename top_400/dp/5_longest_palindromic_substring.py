"""
180 / 180 test cases passed, but took too long. Already O(n^2)

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        type s: str
        :rtype: str
        """
        n = len(s)
        dp = [0 for i in range(n)]
        same = [0 for i in range(n)]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i] = 1
                same[i] = 1

        modified = True
        for k in range(n):
            if modified:
                modified = False
            else:
                break

            for i in range(n - 1):
                if same[i] < same[i + 1] + 1:
                    if i + same[i + 1] + 1 < n and s[i] == s[i + same[i + 1] + 1]:
                        same[i] = same[i + 1] + 1
                        modified = True
            print(same)

        print()
        modified = True
        for k in range(n):
            if modified:
                modified = False
            else:
                break

            for i in range(n - 1):
                if dp[i] < dp[i + 1] + 2:
                    print('in2')
                    if i + dp[i + 1] + 2 < n and s[i] == s[i + dp[i + 1] + 2]:
                        dp[i] = dp[i + 1] + 2
                        modified = True
                if dp[i] < dp[i + 1] + 1:
                    print('in1')
                    if i + dp[i + 1] + 1 < n and s[i] == s[i + dp[i + 1] + 1] and dp[i + 1] == same[i + 1]:
                        dp[i] = dp[i + 1] + 1
                        modified = True
                else:
                    pass
            print(dp)

        max_i = 0
        max_len = 0
        for i in range(n):
            if dp[i] > max_len:
                max_i = i
                max_len = dp[i]

        return s[max_i: max_i + dp[max_i] + 1]


sol = Solution()
s = "ccc"
print(sol.longestPalindrome(s))
