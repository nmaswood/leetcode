"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    """
    Space: O(1)
    Time : O(n)

    Do regular in order traversal the tree. However also store a boolean
    that allows you to know whether a particular child is the left child
    of another node. If this set and the node has no children you know
    that it is a child node and you can add its value to your accumulator.

    """

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.acc = 0

        def f(root, collect):

            if not root:
                return

            f(root.left, True)

            if collect and not root.left and not root.right:
                self.acc += root.val
                return

            f(root.right, False)

        f(root, False)

        return self.acc
