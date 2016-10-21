from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def __init__(self):

        self.min = float('inf')
        self.max = float('-inf')

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        d = defaultdict(list)

        def sub(tree,index):

            if not tree:
                return 

            self.min = min (self.min, index)
            self.max = max (self.max, index)

            d[index].append(tree.val)

            sub(tree.left, i - 1)
            sub(tree.right, i + 1)


        sub(root,0)

        return [d[i] for x in range(self.min, self.max + 1)]        