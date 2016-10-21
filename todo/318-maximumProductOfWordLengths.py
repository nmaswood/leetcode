import heapq

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        heap = []

        for word in words:


        	heapq.heappush(heap, -len(word))


        return heapq.heappop(heap) * heapq.heappop(heap)



r = Solution()

res = r.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])

print (res)