class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)
        total = 0
        l = len(nums)
        for index, num in enumerate(sorted_nums):
            if index == l-1:
                break
            if index % 2 == 0:
                total += num
        return total


test_case = [1,4]

x = Solution()
res = x.arrayPairSum(test_case)
print(res)












