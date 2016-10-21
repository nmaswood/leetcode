from queue import Queue

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.one = Queue()
        self.two = Queue()

    def push(self, x):


        """
        :type x: int
        :rtype: nothing
        """
        
        self.one.put(x)

    def _balance_(self):

        if self.two.empty():

            while not self.one.empty():

                val = self.one.get()

            self.two.put(val)


    def pop(self):

        """
        :rtype: nothing
        """

        self._balance_()

        if not self.two.empty():
            self.two.get()
        

    def top(self):

        """
        :rtype: int
        """

        self._balance_()
        

        

    def empty(self):
        """
        :rtype: bool
        """
        