class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ls = len(s)
        lp = len(p)

        T = [[False for _ in range(ls + 1)] for _ in range(lp + 1)]

        T[0][0] = True

        for i in range(1,ls):
            for j in range(1,lp):

                letter_text, letter_pattern = s[i-1], p[j-1]

                if letter_text == letter_pattern or letter_pattern == '.':
                    T[i][j] = T[i-1][j-1]
                else if (latter_pattern = '*'):
                    T[i][j] = T[i][j-2]
                    letter_text_prev, letter_pattern_prev = s[i-2], p[j-2]

                    if (letter_pattern_prev == '.' or letter_text_prev == letter_patter_prev):
                        T[i][j] = T[i][j] or T[i-1][j]
                else:

                    T[i][j] = False


