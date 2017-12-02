class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        running_total = 0

        for num in nums:
            if num == 1:
                running_total += 1
                max_so_far = max(max_so_far, running_total)
            else:
                running_total = 0

        return max_so_far

x = Solution()
res = x.findMaxConsecutiveOnes([1,1,1,0,1,1,0])
print (res)
