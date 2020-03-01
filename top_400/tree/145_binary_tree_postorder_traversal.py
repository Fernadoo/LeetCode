# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # Recursive
# class Solution(object):
#     def postorderTraversal(self, root):
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
#             ret += self.postorderTraversal(root.left)
#             ret += self.postorderTraversal(root.right)
#             ret.append(root.val)
#             return ret

# Iterative
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        print(root)
        if root == None:
            return []
        ret = []
        call_stack = [root]
        root_stack = []
        num_children_cut_stack = []
        while call_stack != []:
            # print(call_stack)
            curr = call_stack.pop()
            if curr == None:
                num_children_cut_stack[-1] += 1
                while num_children_cut_stack != [] and num_children_cut_stack[-1] == 2:
                    ret.append(root_stack.pop())
                    num_children_cut_stack.pop()
                    if num_children_cut_stack != []:
                        num_children_cut_stack[-1] += 1
            else:
                print(curr.val)
                num_children_cut_stack.append(0)
                root_stack.append(curr.val)
                call_stack.append(curr.right)
                call_stack.append(curr.left)
        while root_stack != []:
            ret.append(root_stack.pop())
        return ret


sol = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
print(sol.postorderTraversal(root))