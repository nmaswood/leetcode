class Solution(object):

    def sum_range(self, lo,hi):

        return sum(range(lo,hi + 1))


    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 1

        lo = min(nums)
        hi= max(nums)

        expected = self.sum_range(lo,hi)
        actual = sum(nums)

        if expected == actual:
            prev = lo - 1
            _next = hi + 1

            if prev > 0:
                return prev
            else:
                return _next
        else:
            return expected - actual

#r = Solution()

#i = [3,4,-1,1]
#x = r.firstMissingPositive(i)

#print (x)
