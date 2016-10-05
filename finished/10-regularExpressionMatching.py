class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        len_string, len_pattern = len(s), len(p)

        T = [[0 for _ in range(len_string + 1)] for _ in range(len_pattern + 1)]

        T[0][0] = True

        for i in range(len_string  + 1 ):
            for j in range(len_pattern + 1):

                if p[j-1] == '*':
                    T[i][j] = T[i][j-2] and T[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
                else:

                    T[i][j] = i > 0 and T[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')

        return T[-1][-1]


