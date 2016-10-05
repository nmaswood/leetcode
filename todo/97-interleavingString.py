class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def f(first, second, third):

            if not first and not second:
                return bool(third)


            word = first if first else second

            copy = list(third)
            isFirst = bool(first)

            first_element, rest = word[0], word[1:]

            for index, letter in enumerate(copy):

                print (letter, first_element)
                if letter == first_element:

                    del copy[index]

                    if isFirst:
                        return f(rest, second, copy)
                    else:
                        return f(None, rest, copy)

            return False

        return f(s1, s2, list(s3))

r = Solution()
res = r.isInterleave('abc', 'ijk', 'aadbbcbcac')
print (res)
