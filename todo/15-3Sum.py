from collections import Counter
from itertools import groupby

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, L, res = sorted(nums), len(nums), []
        for i in range(L - 2):
            # if ith element is the same as i-1th element (say, -1). because -1 has been processed and no duplcate 
            # allowed. So we just continue (skip this element.)
            if nums[i] == nums[i - 1] and i != 0:
                continue
            num = nums[i]
            # left and right pointer
            left, right = i + 1, L - 1
            
            while left < right:
                total = nums[left] + nums[right] + num
            
                if total == 0:
                    # record result.
                    res.append([nums[left], nums[right], num])
                    left += 1
                    right -= 1
                    # skip all duplicate element.
                    while left < right and nums[left] == nums[left - 1] :
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
                elif total > 0:
                    # because total is too big, we need to decrease one element of all 3. And because nums is sorted, only right should be decreased
                    right -= 1
                    # skip all duplicate element.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
                elif total < 0:
                    # same as above.
                    left += 1
                    while left < right and nums[left] == nums[left - 1] :
                        left += 1
        return res


r = Solution()
res = r.threeSum([-1, 0, 1, 2, -1, -4])
print (res)
