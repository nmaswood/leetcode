from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):


        self.minny = float("inf")
        self.maxxy = float("-inf")

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        """
        d = defaultdict(list)

        def sub(root, i):

            self.minny = min(self.minny, i)
            self.maxxy = min(self.minny, i)

            if not root:
                return


            d[i].append(root.val)


            sub(root.left, i - 1)
            sub(root.right,i +1)

        sub(root, 0)
        d = dict(d)
        print (d.keys())

        return [d[i] for i in range(self.minny + 1, self.maxxy + 1)]


