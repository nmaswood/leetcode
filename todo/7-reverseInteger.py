class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0

        as_positive = abs(x)
        rev_int = int(str(as_positive)[::-1])


        return -1 * rev_int if is_negative else rev_int

# r = Solution()

# print (r.reverse(-213))
