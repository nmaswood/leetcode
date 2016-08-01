class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        def swap_values(ori_list, l, r):

            ori_list[l], ori_list[r] = ori_list[r], ori_list[l]

        def get_values(ori_list, l, r):

            return ori_list[l], ori_list[r]

        print (nums)

        len_l = len(nums)
        left = 0
        right = len_l - 1

        while left < right:

            left_val, right_val = get_values(nums, left, right)

            if left_val == val and right_val != val:
                swap_values(nums, left, right)
                left += 1
                right -= 1
            elif left_val == val and right_val == val:
                right -= 1
            else:
                left += 1

        return len_l - nums.count(val)
