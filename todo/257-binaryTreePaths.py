class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):


    	acc = []

    	def sub(tree, soFar):

    		if not tree:

    			print ("fuck")
    			print (soFar)
    			acc.append('->'.join(list(soFar)))
    			return

    		sub(root.left, soFar  + str(tree.val))
    		sub(root.right, soFar  + str(tree.val))

    	sub(root,'')

    	return acc
r = Solution()
res = r.binaryTreePaths(TreeNode(1))
print (res)