class BST():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):

        acc = []

        def f(tree):

            if not tree:
                return

            left,right = tree.left, tree.right
            f(left)
            acc.append(str(tree.val))
            f(right)
        f(self)

        return '\t'.join(acc)

    def insert(self, val):

        def f(tree, value):

            if not tree:
                return BST(val)

            root_val = tree.val
            left, right = tree.left, tree.right

            # if the value is not present don't do anything

            if root_val == value:
                return
            elif root_val >= value:
                return BST(root_val, f(left,value), right)
            else:
                return BST(root_val, left, f(right,value))

        return f(self,val)

    def inorder(self):
        acc = []

        def f(rest):

            if not rest:
                return

            left, right = rest.left, rest.right

            f(left)
            acc.append(rest.val)
            f(right)
        f(self)
        return acc

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):

    def __init__(self):
        self.BST = None

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        bst = self.BST

        if not bst:
            self.BST = BST(val)
        else:
            self.BST.insert(val)

    def getIntervals(self,):
        """
        :rtype: List[Interval]
        """

        acc = []
        nums = self.BST.inorder()

        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [Interval(str(nums[0]), str(nums[0]))]
        else:
            acc = []
            t = [nums[0]]
            start = nums[0]

            for num in nums[1:]:

                if start + 1  == num:
                    t.append(num)
                    start = num
                else:
                    acc.append(t)
                    t = [num]
                    start = num
            acc_prime = acc + [t]

            f = lambda x: (x[0],x[-1])
            values = list(map(f, acc_prime))

            return [Interval(a,b) for a,b in values]

