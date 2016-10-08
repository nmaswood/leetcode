class Solution(object):

    def numDecodings(self, s):

        if not s or  s == '0':
            return 0

        l = len(s)

        DP = [0 for _ in range(l + 1)]
        DP[0] = 1
        
        for i in range(1, l +1):

            if 0 <= int(s[i - 1]) <= 9:


                DP[i] += DP[i-1]

            if i -2 >= 0 and 10 <= int(s[i-1:i + 1]) <= 26:

                DP[i] += DP[i - 2]

        return DP[l]

"""
    def __init__(self):

        self.num = 0

    def numDecodings(self, s):
        if not s or s == '0':
            return 0

        def f(string):

            if not string:

                self.num += 1 
                return

            first_two_letters, first_two_rest = string[:2], string[2:]

            first_letter, first_rest = string[0], string[1:]


            as_int = int (first_two_letters)

            if 10 <= as_int <= 26:

                f(first_two_rest)

            if first_letter != '0':

                f(first_rest)

        f(s)

        return self.num
"""

r = Solution()
res = r.numDecodings('12')
print (res)
