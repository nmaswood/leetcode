import heapq

class MedianFinder:

    def __init__(self):

        self.l = []

    def addNum(self, num):

        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.l, num)

    def isEven(self, x):

        return x % 2 == 0

    def extractKth(self,k):
        copy = list(self.l)

        for _ in range(k):
            res = heapq.heappop(copy)

        return res

    def extractKthandKPlusOne(self,k):
        copy = list(self.l)
        res = 0
        print ('k', k)

        for _ in range(k + 1):
            res = heapq.heappop(copy)

        return res, heapq.heappop(copy)

    def findMedian(self):

        """
        Returns the median of current data stream
        :rtype: float
        """

        l = len(self.l)

        half = int((l - 1) / 2)

        if self.isEven(l):
            a,b = self.extractKthandKPlusOne(half)
            return float(a + b) / 2
        else:
            return self.extractKth(half)

        return self.median()

"""
mf = MedianFinder()
mf.addNum(-1)
mf.addNum(-2)
res = mf.findMedian()
res = mf.findMedian()
res = mf.findMedian()
res = mf.findMedian()
res = mf.findMedian()
print (res)
"""
