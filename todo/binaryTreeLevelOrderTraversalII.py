class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):

        self.result = True

    def height(self, root):
        if not root:
            return 0
        else:
            return  1 + max(self.height(root.left),self.height(root.right))
            
    def isBalanced(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        def f(tree):

            if not tree or not self.result:
                return

            if abs(self.height(tree.left) - self.height(tree.right)) > 1:
                self.result = False

            return f(tree.left) and f(tree.right)

        f(root)

        return self.result






a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

r = Solution()

res = r.isBalanced(a)
print (res)

