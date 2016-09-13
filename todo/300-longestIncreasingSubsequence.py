class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        T = [None for _ in range(l)]

        for i in range(l):
            T[i] = 1
            for j in range(l):

                vali, valj = nums[i], nums[j]
                if vali >= valj and T[j] + 1 > T[i]:
                    T[i] = T[j] + 1

            return T

r = Solution()
res = r.lengthOfLIS([10,9,2,5,3,7,101,18])

print(res)
