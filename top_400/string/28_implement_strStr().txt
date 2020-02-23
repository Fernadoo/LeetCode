'''
Implement strStr().

Return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? 
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when 
needle is an empty string. This is consistent to C's 
strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        h_ptr, n_ptr = 0, 0
        while h_ptr < len(haystack):
            match = 0
            if haystack[h_ptr] == needle[n_ptr]:
                if len(haystack) - h_ptr < len(needle):
                    return -1
                match = 1
                for i in range(len(needle)):
                    if haystack[h_ptr + i] != needle[i]:
                        match = 0
            if match ==1:
                return h_ptr
            else:
                h_ptr += 1
                n_ptr = 0
        return -1

# # Recommended solution
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         sl = len(needle)
#         if sl == 0:
#             return 0
#         i=0
#         while i < len(haystack)-sl+1:  
#             if haystack[i] == needle[0]:
#                 sub = haystack[i:i+sl]
#                 if sub == needle:
#                     return i
#             i+=1
#         return -1


sol = Solution()
haystack = "aaa"
needle = "aaa"
print(sol.strStr(haystack, needle))
