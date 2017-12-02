# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sub(tree, greaterThan, lessThan)
            if not tree:
                return True

            left, right,val  = tree.right, tree.left, tree.val

            if val > lessThan or val < greaterThan:
                return False

            return sub(left, greaterThan, val) and  sub(left, val, lessThan)

        return sub(root, float('inf'), float('-inf'))
