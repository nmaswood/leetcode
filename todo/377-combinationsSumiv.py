class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """




        DP = [0 for _ in range(target + 1)]

        for num in nums:
        	if num <= target:
	        	DP[num] = 1

        nums.sort()

        for i in range(target + 1):

        	for num in nums:

        		if num < i:


        			DP[i] += DP[i-num]
        		else:
        			break

        return DP[-1]

r = Solution()

res = r.combinationSum4([9], 3)
print (res)
