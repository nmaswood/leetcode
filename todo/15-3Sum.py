from collections import Counter
from itertools import groupby

class Solution(object):

    def twoSum(self, counted, target):

        skip = set()

        sols = []

        for k,v in counted.items():

            if k not in skip:

                need = target - k

                if need in counted:

                    if need == k and counted[k] == 1:
                        pass
                    else:
                        sols.append([k,need])
                        skip.add(need)

        return sols

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        v = Counter(nums)

        sols = []

        skip = set()

        for key, value in v.items():

            sub_sols = self.twoSum(v, -key)

            if sub_sols:
                sols += [[key] + x for x in sub_sols]

        sorted_sols = sorted(sols)
        dedup = [sorted_sols[i] for i in range(len(sols)) if i == 0 or sorted_sols[i] != sorted_sols[i-1]]
        return dedup

r = Solution()
r.threeSum([-1,0,1,2,-1,-4])
