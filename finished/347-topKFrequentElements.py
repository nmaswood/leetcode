from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        """

        counted = Counter(nums)

        return [pair[0] for pair in counted.most_common(k) ]
        


r = Solution()
res = r.topKFrequent([1,1,1,2,2,3], 2)
print (res)
