from math import log

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return True

        left = 0
        right = num

        max_iteratiions = round(log(num, 2) + 1)

        iterations = 0


        while left < right and iterations < max_iteratiions:

            mid = (left + right) / 2

            print (mid)
            value = mid ** 2


            if value == num:


                print (value, num)
                return True
            elif value < num:
                left = mid
            else:
                right = mid

            iterations += 1

        return False


r = Solution()

res = r.isPerfectSquare(16)
print(res)

