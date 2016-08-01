from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        majority_num = len(nums) / 2
        for k,v in c.items():
            if v > majority_num:
                return k
        assert False