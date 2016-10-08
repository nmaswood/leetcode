class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        seen = {}
        acc = 0
        res = float("-inf")
        for i, num in enumerate(nums):
            acc += num

            if num not in seen:
                seen[acc] = i
            elif acc - k in seen:
                res = max(res, i - seen[acc -k])

        return res




r = Solution()

res = r.maxSubArrayLen([1,-1,5,-2,3], 3)

print (res)
