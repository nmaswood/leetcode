class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        expected = set(range(len(nums) + 1))
        actual = set(nums)


        print (expected)
        print (actual)
        diff = expected - actual


        return diff.pop()

r = Solution()

res = r.missingNumber([0,1,3])

print (res)
