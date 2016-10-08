class NumArray(object):
    def __init__(self, nums):

        """
        initialize your data structure here.
        :type nums: List[int]
        """
        acc = 0
        T = [0 for _ in nums]

        for index, num in enumerate(nums):

            if index == 0:
                T[0] = num
            else:
                T[index] = T[index-1] + num

        self.values = T
        self.nums = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.values[j] - self.values[i] + self.nums[i]


numArray = NumArray([-2,0,3,5,2,-1])

