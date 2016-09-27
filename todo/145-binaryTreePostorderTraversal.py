# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        acc = []

        s = []

        if root is None:
            return []

        s.append(root.left)
        s.append(root.val)
        s.append(root.right)

        while s:

            val = s.pop()

            if val is None:
                continue
            elif isinstance(val, int) or isinstance(val, float):
                acc.append(val)
            else:
                s.append(root.left)
                s.append(root.val)
                s.append(root.right)

        return acc








