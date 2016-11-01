"""
See if a list of integers can be broken into two seperate partitions


[1,2,3,4, 2,2]  -> [[2,2,2,1], [3,4]]


"""
class Solution():

	def __init__(self):
		pass

	def dp(self,nums):

		s = sum(nums)

		desired_value = s / 2

		DP = [0 for _ in range(desired_value + 1)]

		DP[0] = True

		for i in range(desired_value + 1):

			for num in nums:

				if (i  - num) > 0 and DP[i-num]:


					DP[i] = True

		return DP[-1]



	def pluck(self, nums, i):

		return ([num for (idx, num) in enumerate(nums) if idx != i], nums[i])


	def brute_force(self,nums):

		self.solutions = set()

		def recurse(set_1_numbers, set_2_numbers):

			if not set_1_numbers:
				return

			if sum(set_1_numbers) == sum(set_2_numbers):


				self.solutions.add(

					tuple(
						tuple(set_1_numbers),
						tuepl(set_2_numbers)
						)
					)


			for (idx,num) in enumerate(set_1_numbers):


				plucked,num_removed = self.pluck(set_1_numbers, idx)

				set_1_prime = plucked

				set_2_prime = set_2_numbers[:] + [num_removed]

				recurse(set_1_prime, set_2_prime)

		return self.solutions





































