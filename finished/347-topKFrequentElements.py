from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = sorted(list(Counter(nums).items()), key = lambda x: x[1], reverse = True)

        return [k for k,v in  c[:k]]


r = Solution()
res = r.topKFrequent([1,1,1,2,2,3], 2)
