'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an 
integer pos which represents the position (0-indexed) in 
the linked list where tail connects to. If pos is -1, then 
there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        while curr != None:
            print(curr.val)
            if curr.val == 99999:
                return True
            curr.val = 99999
            curr = curr.next
#         return False

# # Genius approach
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head == None:
#             return False
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if fast == None or fast.next == None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True


sol = Solution()
head = ListNode(1)
n1 = ListNode(32)
n2 = ListNode(4)
n3 = ListNode(2)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n1
print(sol.hasCycle(head))       