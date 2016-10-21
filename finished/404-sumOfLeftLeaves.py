# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):

        self.acc = 0 

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
                if not root.left and not root.right:
                    self.acc += root.val
                    return

            f(root.right, False)

        f(root, False)

        return self.acc












