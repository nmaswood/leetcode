from pdb import set_trace
import heapq

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def findSecondMinimumValue(self, root):

        min_1 = None
        min_2 = None

        stack = [root]
        seen = set()

        while stack:
            value = stack.pop()

            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)

            the_val = value.val
            #set_trace()


            if min_1 is None:
                min_1 = the_val

            elif min_1 and min_2 is None:
                if the_val <= min_1:
                    min_2 = min_1
                    min_1 = the_val
                else:
                    min_2 = the_val
            elif the_val <= min_1:
                min_2 = min_1
                min_1 = the_val
            elif the_val <= min_2:
                min_2 = the_val
        return min_2

    def _findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = []

        stack = [root]

        while stack:
            value = stack.pop()

            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)

            heapq.heappush(h,value.val)


        print (h)
        s = set()
        h = [x for x in

        return heapq.nsmallest(2, h)[1]

a = TreeNode(4)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(0)

a.left = b
#a.right = c
#c.left = d
#d.right = e

inst = Solution()
res = inst.findSecondMinimumValue(a)
print (res)

