import heapq

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

        return heapq.heappop(heap)

r = Solution()
res = r.findMin([4,5,6,7,0,1,2])
print (res)

