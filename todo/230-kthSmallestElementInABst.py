# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        acc = []

        def f(root):

            if root is None or len(acc)  - 1 >  k:
                return

            f(root.left)
            acc.append(root.val)
            f(root.right)
        f(root)
        print(acc)

        return acc[-1]
