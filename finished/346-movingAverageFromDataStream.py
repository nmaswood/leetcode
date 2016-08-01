class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.total = 0
        self.n = 0
        self.numbers_reversed = []

    def next(self, val):

        """
        :type val: int
        :rtype: float
        """

        if self.n == self.size:
            subtract_me = self.numbers_reversed.pop(0)
            self.total += val - subtract_me
        else:
            self.total += val
            self.n += 1

        self.numbers_reversed.append(val)
        return float(self.total) / float(self.n)

def testing():

    m = MovingAverage(3)
    print (m.next(1))
    print (m.next(10))
    print (m.next(3))
    print (m.next(5))

testing()
