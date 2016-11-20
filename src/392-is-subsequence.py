"""
392 is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    s = "abc", t = "ahbgdc"

    Return true.

Example 2:
    s = "axc", t = "ahbgdc"

    Return false.
"""

class Solution(object):
    def isSubsequence(self, s, t):

        """
        Explanation:

        1. check if s is the empty string or if it is longer than t
        2. otherwise walk through each char in string t
        3. use an index to keep track of the letters you want to see in s
        4. every time you see a letter you  need s increment i  and look for the next letter
        5. after you have finished iterating check if you have seen all of s in t


        Space: O(1)
        Time: O(n)

        :type s: str
        :type t: str
        :rtype: bool
        """

        len_s = len(s)
        len_t = len(t)

        if len_s == 0:
            return True
        elif len_s > len_t:
            return False

        s_index = 0

        for (t_index, t_char) in enumerate(t):

            if s_index >= len_s:
                break

            if s[s_index] == t_char:
                s_index += 1

        return s_index == len_s - 1

r = Solution()
s, t = "abc", "ahbgdc"
s, t = "axc", "ahbgdc"
res = r.isSubsequence(s,t)
print (res)
