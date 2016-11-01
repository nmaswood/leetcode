class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        costs = [0 for _ in range(len(nums))]
        costs[0] = nums[0]

        costs[1] = nums[1]


        for i, num in enumerate(nums[2:]):
            i = i + 2
            costs[i]  = max(

                costs[i-2] + num,
                costs[i-1]
            )

        return costs[-1]

r = Solution()
res = r.rob([1,1])
print (res)


