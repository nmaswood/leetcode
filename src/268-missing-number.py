class Solution(object):

    def missingNumber(self, nums):

        expected = set(range(len(nums) + 1))

        actual = set(nums)

        return (expected - actual).pop()

r = Solution()
res = r.missingNumber([0,1,3])
