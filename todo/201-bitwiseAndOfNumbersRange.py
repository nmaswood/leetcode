class Solution(object):
    def rangeBitwiseAnd(self, m, n):

        """
        :type m: int
        :type n: int
        :rtype: int
        """

        acc = ~0
        if abs(m-n) > 1000: return 0

        for x in range(m,n+1):

            acc &= x

        return acc
