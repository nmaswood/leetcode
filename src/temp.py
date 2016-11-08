"""
412. Fizz Buzz
Write a program that outputs the string representation of numbers 1 to n

* multiples of three it should output “Fizz”
* five output “Buzz”.
* For numbers which are multiples of both three and five output “FizzBuzz”.

"""

class Solution(object):

    def fizzBuzz(self, n):
        """
        Explanation:

        For iterate through the numbers [1,n] and for each number
        check what numbers it is divisible by.

        Time : O(n)
        Space: O(n)
        :type n: int
        :rtype: List[str]
        """

        acc = []

        for i in range(1, n+1):

            if i % 15 == 0:
                acc.append("FizzBuzz")
            elif i % 3 == 0:
                acc.append("Fizz")
            elif i % 5 == 0:
                acc.append("Buzz")
            else:
                acc.append(str(i))

        return acc


r = Solution()
res = r.fizzBuzz(15)

print (res)