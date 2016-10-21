class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        acc = []

        for i in range(1,n + 1):


            if i % 15 == 0 :
                acc.append('FizzBuzz')

            elif i % 3  == 0 and i % 5 == 0:
                acc.append('Fizz')
                acc.append('Buzz')

            elif i % 3 == 0:
                acc.append("Fizz")

            elif i % 5 == 0:
                acc.append('Buzz')
            else:
                acc.append(str(i))

        return acc

r = Solution()

res = r.fizzBuzz(15)

print (res)