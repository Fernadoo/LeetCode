# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # Recursive
# class Solution(object):
#     def preorderTraversal(self, root):
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
#             ret.append(root.val)
#             ret += self.preorderTraversal(root.left)
#             ret += self.preorderTraversal(root.right)
#             return ret

# Iterative
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        call_stack = [root]
        while  call_stack != []:
            # print(call_stack)
            curr = call_stack.pop()
            if curr == None:
                pass
            else:
                # print(curr.val)
                ret.append(curr.val)
                call_stack.append(curr.right)
                call_stack.append(curr.left)
        return ret        

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
print(sol.preorderTraversal(root))

