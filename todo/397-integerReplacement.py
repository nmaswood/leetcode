class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):

            if n == 0:
                assert False
            elif n == 1:
                return 0
            elif n % 2 == 0:
                return 1 + f(n/2)
            else:
                return 1 + f(n-1)

        return f(n)
