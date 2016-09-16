from collections import Counter
from itertools import groupby

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sols = set()

        l = len(nums)

        nums = sorted(nums)

        for i in range(l - 2):
            start = nums[i]
            left = i + 1
            right = l - 1
            while left < right:

                val1 = nums[left]
                val2 = nums[right]

                sum_val = val1 + val2

                diff = start + val1 + val2 == 0

                if diff:

                    sols.add(tuple(sorted((start, val1, val2))))
                    left +=1

                elif diff < 0:

                    left += 1
                else:
                    right -= 1
        return list(sols)

r = Solution()
res = r.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
print (res)
