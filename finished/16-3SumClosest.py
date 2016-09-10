class Solution(object):

    def diff(self, the_sum, target):

        return abs(the_sum - target)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s = sorted(nums)

        l = len(s)

        left = 0
        right = l - 1
        right_prime = l - 2
        MIN = 1e10

        array = []

        toggle_array = [1,0]
        toggle_right_prime = 1

        while left < right and left < right_prime:

            left_val, right_val, right_val_prime = [s[i] for i in [left, right, right_prime]]


            the_sum = sum([left_val, right_val, right_val_prime])

            the_diff = self.diff(the_sum, target)

            if the_diff < MIN:
                MIN = the_diff
                array = [left_val, right_val, right_val_prime]

            if the_sum >= target:
                if toggle_right_prime:
                    right_prime -= 1
                else:
                    right -= 1
                toggle_right_prime = toggle_array[toggle_right_prime]
            else:
                left += 1

        return sum(array)


r = Solution()
r.threeSumClosest([0,2,1,-3], 1)
