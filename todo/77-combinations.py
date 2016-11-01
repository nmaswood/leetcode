class Solution():

	def __init__(self):
		pass

	def combination_sum(self,nums, target):

		l = len(nums)

		DP = [float("inf") for _ in range(target + 1)]

		for num in nums:
			DP[num] = 1

		for i in range(target):

			for num in nums:

				if num < i:

					DP[i] += DP[i-num]

		return DP[-1]













