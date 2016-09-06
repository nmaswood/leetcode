class Solution(object):

    def noDup(self, s):
        seen = set()
        for l in s:
            if l in seen:
                return False
            seen.add(l)
        return True

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {l: (False, None) for l in s}
        maxNum = 0
        curr = 0
        ls = set()

        index = 1
        for total_index, letter in enumerate(s):
            present, val = d[letter][0], d[letter][1]

            if present:
                curr -= val
                index = 1
                for letter_prime in s[:total_index + 1]:
                    d[letter_prime] = (False, None)
            else:
                curr += 1
                index += 1

            d[letter] = (True,index)

            print ('letter:', letter,d, 'max', maxNum, 'curr', curr, 'val', val)
            if curr > maxNum:
                maxNum = curr

        return maxNum


r = Solution()
s = "pwwkew"
s1 = 'abcabcbb'
print (r.lengthOfLongestSubstring(s))
