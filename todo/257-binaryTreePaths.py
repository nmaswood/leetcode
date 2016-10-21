# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):


    	acc = []

    	def sub(tree, soFar):

    		if not tree:
    			acc.append('->'.join(soFar))
    			return

            newList = soFar[:] 
            newList.append(str.val)

    		sub(root.left, newList[:])
    		sub(root.right, newList[:]

    	sub(root,'')

    	return acc