"""
17. Letter Combinations of a Phone Number


Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""
class Solution(object):

    def __init__(self):

        self.d = {
            "0": "_",
            "1": None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits):

        """
        Explanation:
        Recursively build out a tree structure
        for the string "23" and collect all the paths
        to leaf nodes

        2  -> "abc" , 3 -> "def"

                    ROOT
                /    |     \
            a        b      c
        /   |  \   / | \  / | \
        d   e   f  d  e f d e f

        Time : O(exp)
        Space: O(exp)


        :type digits: str
        :rtype: List[str]
        """
        combinations = set()

        def recurse(_digits, acc):
            if not _digits:
                combinations.add(acc)
                return

            first, rest = _digits[0], _digits[1:]

            chars = self.d[first]

            for char in chars:

                recurse(rest, acc + char)

        recurse(digits, '')

        return combinations


r = Solution()
res = r.letterCombinations('23')
print (res)



