# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            print("null")
            return ret
        else:
            print(root.val)
            ret.append(root.val)
            ret += self.preorderTraversal(root.left)
            ret += self.preorderTraversal(root.right)
            return ret 

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
print(sol.preorderTraversal(root))