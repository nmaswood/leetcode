# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):

        left, right = root.left, root.right
        l = ''

        if not left and not right:
            return 'None - None'
        elif not left:
            return 'None - ' + str(right.val)
        elif not right:
            return str(left.val) + ' - None'

        return str(root.left) + ' - ' + str(root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return True

        left, right = self.helper(root.left), self.helper(root.right)

        if left != right:
            return False
        return self.isSymmetric(root.left) and self.isSymmetric(root.right)

