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
        while(start>=0 and end < len(string) and string[start]==string[end]):
            start -= 1
            end += 1
        return string[start+1:end]

    def shortestPalindrome(self, s):

        if s == s[::-1]:
            return s

        longest = self.longestPalindrome(s)
        length = len(longest)

        left_index = s.index(longest)
        right_index = left_index + length - 1 if length else 0


        print ('ori', s, 'longest', longest, 'length', length, 'left', left_index, 'right',
               right_index, 'new', s[:])

        return s[right_index + 1:][::-1] + s


        """
        if i > len(s) / 2:
            print ("c")
            return s[i:]  + s
        else:
            print ("d")
            print (s[:i])
            return s + s[:i]
        """

r = Solution()
res = r.shortestPalindrome('abb')
print (res)
