# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import queue
        output = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            level = queue.Queue()
            level_output = []
            while not q.empty():
                tmp = q.get()
                if tmp == None:
                    continue
                level_output.append(tmp.val)
                level.put(tmp.left)
                level.put(tmp.right)
            if level_output != []:
                output.append(level_output)
            q = level
        return output


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(8)
print(sol.levelOrder(root))