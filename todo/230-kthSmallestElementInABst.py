# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):

        self.seen = 0
        self.done = False
        self.k = 0
        self.val = 0


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        acc = []

        def f(root):

            if root is None or self.done:
                return

            f(root.left)
            if self.seen == k:
                self.val = root.val
                self.done = True
                return
            self.seen += 1

            f(root.right)
        f(root)
        return self.val
