from collections import defaultdict()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def __init__(self):

		self.min = float("inf")
		self.max = float("-inf")

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        d = defaultdict(list)

        def traverse(tree, level):

        	if not tree:
        		return 

        	self.min = min(self.min, level)
        	self.max = max(self.max, level)

        	d[t].append(tree.val)

        	traverse(tree.left, level + 1)
        	traverse(tree.right, level + 1)

        traverse(root, 0)
       	return [d[i] for i in range(self.min, self.max + 1, -1)]

        