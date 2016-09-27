# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        acc = []

        def f(root, collect):

            if not root:
                return

            f(root.left, True)
            if collect:
                acc.append(root.val)
            f(root.right, False)
        f(root, False)

        return sum(acc)












