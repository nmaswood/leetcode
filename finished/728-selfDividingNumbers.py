class Solution(object):

    @staticmethod
    def _isSelfDividingNumbers(number):
        digits = [int(x) for x in list(str(number))]

        for digit in digits:
            print (number, digit)
            if digit == 0 or number % digit != 0:
                return False

        return True

    def selfDividingNumbers(self, left, right):

        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        return [num for num in range(left, right + 1) if Solution._isSelfDividingNumbers(num)]


if __name__ == "__main__":
    inst = Solution()
    res = inst.selfDividingNumbers(1, 22)
    print (res)

