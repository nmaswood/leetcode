# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def __init__(self):

		self.min = float('inf')

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sub(tree, soFar):

        	if not tree:
        		self.min = min (self.min, soFar)

        	sub(root.left, soFar + 1)
        	sub(root.right, soFar + 1)

        sub(root, float('inf'))

        return self.min        