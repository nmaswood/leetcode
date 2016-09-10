class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = 0
        curr = 0

        for num in nums:
            temp = curr
            curr = max(prev + num, curr)
            prev = temp
        return curr
r = Solution()
res = r.rob([1,2,3,4])
print (res)


