# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
            ret += self.postorderTraversal(root.left)
            ret += self.postorderTraversal(root.right)
            ret.append(root.val)
            return ret

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
print(sol.postorderTraversal(root))