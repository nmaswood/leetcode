class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def sub(n, acc):

            if n == 1:
                return acc
            else:

                accPrime = set()

                for item in acc:

                    for s in ('({})','(){}', '(){}'):

                        accPrime.add(s.format(item))

                return sub(n-1,accPrime)

        return sub(n, set(['()']))



r = Solution()

x = r.generateParenthesis(3)
print (x)

["((()))","()(())","(())()","(()())","()()()","()()()","(()())","()()()","()()()"]

["((()))","(()())","(())()","()(())","()()()"]