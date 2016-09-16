import heapq

class HitCounter(object):

    def __init__(self):

        h = []
        heapq.heapify(h)
        self.heap = h
        self.size = 0
        self.MAX = -1

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """

        heapq.heappush(self.heap, timestamp)
        self.size += 1
        self.MAX = max(self.MAX, timestamp)



    def getHits(self, timestamp):

        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        heap_peek = self.heap[0]
        diff = (timestamp - heap_peek)
        print (diff)

        while timestamp - heap_peek >= 300 and self.size:

            other_val = heapq.heappop(self.heap)
            diff = timestamp - other_val
            heap_peek = self.heap[0]
            self.size  -= 1

        return self.size


obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
obj.hit(300)

param_2 = obj.getHits(301)
print (param_2)
