class NumArray(object):
    def __init__(self, nums):

        """
        initialize your data structure here.
        :type nums: List[int]
        """
        l = len(nums)
        d = {}
        for i in range(l):
            s = 0
            for j in range(l):
                s += nums[j]
                d[(i,j)] = s
        self.d = d
        print (self.d)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.d[(i,j)]



numArray = NumArray([-2,0,3,5,2,-1])

