class Solution(object):
    def findRepeatedDnaSequence(self, s):

        d = {}
        len_s = len(s)

        if len_s < 11:
            return []

        for i in range(len_s - 10):

            window = s[i:i + 10]
            d[window] = d.get(window, 0) + 1
        return [k for k,v in d.items() if k >= 2]

