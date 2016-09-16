# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def f(curr,prev, acc,s):
            if not curr:
                return acc

            sPrime = s + root.val
            prevPrime  = prev + [sPrime]

            accPrime = acc

            if sPrime == target:
                print (sPrime, target)
                accPrime = acc + [root.val]

            return f(curr.left, prevPrime, accPrime, sPrime) +  f(curr.right, prevPrime, accPrime, sPrime)

        return f(root, [], [], 0)
