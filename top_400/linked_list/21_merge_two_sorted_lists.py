'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         ptr_1, ptr_2 = l1, l2
#         output = None
#         def add_node(prev, node):
#             if prev == None:
#                 return node
#             else:
#                 curr = prev
#                 while curr.next != None:
#                     curr = curr.next
#                 curr.next = node
#                 return prev
#         while ptr_1 != None or ptr_2 != None:
#             if ptr_1 != None and ptr_2 != None:
#                 print(ptr_1.val, ptr_2.val)
#                 if ptr_1.val < ptr_2.val:
#                     output = add_node(output, ListNode(ptr_1.val))
#                     ptr_1 = ptr_1.next
#                 else:
#                     output = add_node(output, ListNode(ptr_2.val))
#                     ptr_2 = ptr_2.next
#             elif ptr_1 == None and ptr_2 != None:
#                 print(None, ptr_2.val)
#                 output = add_node(output, ptr_2)
#                 ptr_2 = None
#             elif ptr_1 != None and ptr_2 == None:
#                 print(ptr_1.val, None)
#                 output = add_node(output, ptr_1)
#                 ptr_1 = None
#             print('output: ', output)
#         return output


# Recursive
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr_1, ptr_2 = l1, l2
        if ptr_1 == None:
            return ptr_2
        elif ptr_2 == None:
            return ptr_1
        if ptr_1.val < ptr_2.val:
            merged = self.mergeTwoLists(ptr_1.next, ptr_2)
            ptr_1.next = merged
            return ptr_1
        else:
            merged = self.mergeTwoLists(ptr_1, ptr_2.next)
            ptr_2.next = merged
            return ptr_2



sol = Solution()
l1 = ListNode(1); l1.next = ListNode(2); l1.next.next = ListNode(4)
# l2 = None
l2 = ListNode(1); l2.next = ListNode(3); l2.next.next = ListNode(4)
print(sol.mergeTwoLists(l1, l2))

