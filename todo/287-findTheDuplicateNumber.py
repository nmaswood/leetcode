class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        the_max = max(nums)

        the_range = range(1,the_max+1)

        s_expected = sum(the_range)
        l_expected = len(the_range)


        s_actual = sum(nums)
        l_actual = len(nums)

        sum_difference = s_actual - s_expected
        l_difference = l_actual - l_expected


        return sum_difference / l_difference

r  = Solution()

i = [1,4,4,2,4]

res = r.findDuplicate(i)

print (res)



