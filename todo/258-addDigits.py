class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        x = num % 9
        if (x == 0 and num > 0):
            return 9
        return x

