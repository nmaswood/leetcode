class Solution(object):


    def __init__(self):

        self.values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L':50,
            'C': 100,
            'D': 500,
            'M':1000
        }

        self.order = {
            'I': set(['V', 'X']),
            'V': set(['X']),
            'X': set(['L', 'C']),
            'L': set(['C']),
            'C': set(['D','M']),
            'D': set(['M']),
            'M': set(['none'])
        }

        self.seen = set()

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        acc = 0

        print (s[::-1])

        for letter in s[::-1]:

            val = self.values[letter]
            opposite = self.order[letter]

            if opposite & self.seen:
                val *= -1

            acc += val
            self.seen.add(letter)

        return acc



r = Solution()
r.romanToInt("MMCCCXCIX")


