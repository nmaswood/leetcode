class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def f(string):

            length = len(string)

            if length in [0,1]:
                return length
            else:
                first, first_rest = string[0], string[1:]
                second, second_rest = string[:2], string[2:]

                if first == '0':
                    return f(first_rest)


                if int(second) <= 26:
                    return 1+ f(first_rest) + f(second_rest)
                else:
                    return 1 + f(first_rest)

        return f(s)
