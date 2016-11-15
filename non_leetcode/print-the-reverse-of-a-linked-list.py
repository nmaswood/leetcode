class List():

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution():

    def printReverse(self, linkedList):

        stack = []

        while (linkedList):

            stack.append(linkedList.val)
            linkedList = linkedList.next

        while stack:
            print(stack.pop())

    def printReverseCallStack(self, linkedList):

        def f(l):

            if not l:
                return

            f(l.next)
            print(l.val)

        f(linkedList)
