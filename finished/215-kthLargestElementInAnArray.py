import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:

            heapq.heappush(heap, -num)

        for _ in range(k):
            res = heapq.heappop(heap)

        return res * -1

r = Solution()
res = r.findKthLargest([2,1], 1)
print (res)
