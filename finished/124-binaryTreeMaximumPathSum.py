# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def __init__(self):

		self.max = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(t, soFar):

        	if not t:
        		self.max = max(self.max, soFar)

        	val = t.val

        	traverse(root.left, val  + soFar)
        	traverse(root.right, val  + soFar)

        traverse(root, 0)

        return self.max