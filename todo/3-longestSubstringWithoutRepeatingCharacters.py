class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        if l == 0:
            return 0

        m = [0] * l

        seen = set()

        last_char = ''

        for i,letter in enumerate(s):

            if i == 0:
                m[i] = 1
                seen.add(letter)
            elif letter not in seen:
                seen.add(letter)
                m[i] = m[i-1] + 1
            else:
                seen = set()
                seen.add(letter)
                m[i] = 1
                if last_char != letter:
                    m[i] += 1

            last_char = letter

        print (m)
        return max(m)

r = Solution()
s = "abcabcbb"
print (r.lengthOfLongestSubstring(s))
