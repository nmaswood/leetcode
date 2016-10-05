class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        l = len(s)
        if l <= 2:
            return '' if (s[0] != s[l-1]) else s

        result = ''
        for i in range(0,l):
            palindrome = self.SearchPalindrome(s, i, i)

            if len(palindrome) > len(result):
                result = palindrome

            palindrome = self.SearchPalindrome(s, i, i+1)

            if len(palindrome) > len(result):
                result = palindrome
        return result

    def SearchPalindrome(self, string, start, end):
        while (start>=0 and end < len(string) and string[start]==string[end]):
            start -= 1
            end += 1
        return string[start+1:end]

    def shortestPalindrome(self, s):

        if s == s[::-1]:
            return s

        sub = self.longestPalindrome(s)
        len_sub = len(sub)
        idx = s.index(sub)

        single = False

        if not sub:
            single = True
            sub = s[0]

        print ('sub', sub)
        print ('idx', idx)
        print ('len_sub', len_sub)
        print ('first', s[len_sub:][::-1])

        if single:
            return s[1:][::-1] + s
        if idx == 0:

            return s[len_sub:][::-1] + s
        else:
            return s[1:][::-1] + s


r = Solution()
res = r.shortestPalindrome("abb")
print (res)
