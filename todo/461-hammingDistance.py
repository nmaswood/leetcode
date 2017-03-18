class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xored = x ^ y
        as_bin_str = bin(xored)

        return as_bin_str.count("1")
