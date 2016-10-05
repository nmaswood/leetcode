from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomLetters = Counter(ransomNote)
        magazineLetters = Counter(magazine)


        for ransomLetter, ransomLetterCount in ransomLetters.items():

            if ransomLetter not in magazineLetters:
                return False

            if ransomLetterCount > magazineLetters[ransomLetter]:
                return False

        return True


