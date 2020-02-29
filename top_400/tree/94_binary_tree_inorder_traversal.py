# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # Recursive
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         ret = []
#         if root == None:
#             print("null")
#             return ret
#         else:
#             print(root.val)
#             ret += self.inorderTraversal(root.left)
#             ret.append(root.val)
#             ret += self.inorderTraversal(root.right)
#             return ret

# Iterative
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        call_stack = [root]
        root_stack = []
        while  call_stack != []:
            # print(call_stack)
            curr = call_stack.pop()
            if curr == None:
                if root_stack != []:
                    ret.append(root_stack.pop())
                else: 
                    pass
            else:
                print(curr.val)
                root_stack.append(curr.val)
                call_stack.append(curr.right)
                call_stack.append(curr.left)
        return ret  


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sol.inorderTraversal(root))