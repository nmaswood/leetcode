class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if all([x < 0 for x in nums]):
            return max(nums)

        l = len(nums)


        b = [0] * l

        for i in range(l):

            val = nums[i]

            if i == 0:
                if val > 0:
                    b[i] = val
            else:
                opt = b[i-1]
                if opt + val > 0:
                    b[i] = opt + val

        MAX = max(b)
        argmax = b.index(MAX)
        for idx in range(argmax, -1,-1):
            val = b[idx]
            if val <= 0:
                idx += 1
                break

        array = nums[idx:argmax + 1]


        return sum(array)

r = Solution()
res = r.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)

