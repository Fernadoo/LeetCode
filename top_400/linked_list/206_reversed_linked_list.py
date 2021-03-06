'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        output = ""
        curr = self
        while curr != None:
            output = output + str(curr.val) + "-> "
            curr = curr.next
        output += "NULL"
        return output

# # Iterative
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         slow = None
#         mid, fast = head, head
#         # print(mid)
#         while fast != None:
#             fast = mid.next
#             mid.next = slow
#             slow = mid 
#             mid = fast
#             # print(slow)
#         return slow

# Recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        without_head = head.next
        reverse_without_head = self.reverseList(without_head)
        head.next.next = head
        head.next = None
        return reverse_without_head

sol = Solution()
x_1, x_2, x_3, x_4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
x_1.next = x_2
x_2.next = x_3
x_3.next = x_4
# print(x_1)
print(sol.reverseList(x_1))
