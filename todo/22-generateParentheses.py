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
                print ('n', n)
                new = []
                for item in acc:
                    new.append('(' + item + ')')
                    new.append('()' + item)
                    new.append(item + '()')

                return sub(n - 1, new + acc)

        res = set(sub(n, ['()']))

        return [x for x in res if x.count('(') == n]

r = Solution()

x = r.generateParenthesis(3)
print (x)
