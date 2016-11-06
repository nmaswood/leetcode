import heapq

class Solution(object):
    """
    Explanation:

    Simply walk through the list and put elements on heap 

    Then use built in heap methods to return k largest

    * Note python does not hax a max heap, it only has 
    a min heap therefore we mulitiply each element by 
    -1 when we insert it and multiply by negative 1 at the
    end as well

    Space: O(n)
    Time : O(n) ln(k)


    Ex.

    r.findKthLargest([1,24,43,1,4,123,4,12,34,5], 2) ---> 43
    because 43 is the second to largest

    """
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
res = r.findKthLargest([1,24,43,1,4,123,4,12,34,5], 2)
print (res)
