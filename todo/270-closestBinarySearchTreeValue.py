# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def __init__(self):

		self.min = float('inf')

    def closestValue(self, root, target):

        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def sub(tree):

        	if not tree:
        		return

        	self.min = min(self.min, abs(root.val - target))

        	f(root.left, target)
        	f(root.right, target)

       	sub(root)

       	return self.min
