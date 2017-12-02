# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".

class Solution(object):

    # they are are cases where second and other are the same

    def checkCondition(self, idx, first, second, other):
        if idx == 1:
            if not first and second:
                return False
        else:

            if first and second and not other:
                return False
            elif not first and not second and other:
                return False
            elif first and not second and other:
                return False

        return True

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if not word:
            return True

        first = None
        second = None

        for idx, letter in enumerate(word):
            isUpper = letter.isupper()

            if idx == 0:
                first = isUpper
                continue
            elif idx == 1:
                second = isUpper

            if not self.checkCondition(idx, first, second, isUpper):
                return False

        return True

inst = Solution()
word = 'ballS'
res = inst.detectCapitalUse(word)
print (word, res)
