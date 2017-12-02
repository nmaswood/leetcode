from queue import Queue

class TreeNode():

    def __init__(self, x):
        self.root = x
        self.left = None
        self.right = None

class Solution():

    def isSameTree(self, p, q):

        queueOne = Queue()
        queueTwo = Queue()

        queueOne.put(p)
        queueTwo.put(q)

        while not queueOne.empty() and not queueTwo.empty():

            valOne = queueOne.get()
            valTwo = queueTwo.get()

            if valOne.root != valTwo.root:
                return False

            leftOne, rightOne = valOne.left, valOne.right
            leftTwo, rightTwo = valTwo.left, valTwo.right

            if leftOne:
                queueOne.put(leftOne)
            if rightOne:
                queueOne.put(rightOne)

            if leftTwo:
                queueTwo.put(leftTwo)
            if rightTwo:
                queueTwo.put(rightTwo)

        return queueOne.empty() and queueTwo.empty()
