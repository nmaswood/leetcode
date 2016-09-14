import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):

        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = []
        i = 0

        for l in matrix:

            for element in l:

                heapq.heappush(h, (element, i))
                i += 1

        for i in range(k):
            val = heapq.heappop(h)

        return val[0]

r = Solution()

res = r.kthSmallest([
    [1,5,9],
    [10,11,13],
    [12,13,15]
], 8)

print (res)



