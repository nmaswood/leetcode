class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
            
        s_lower = s.lower()
        all_letters = set("Thequickbrownfoxjumpsoverthelazydog0123456789".lower())
        s_prime = ''.join([x for x in s_lower if x in all_letters])
            
        return s_prime == s_prime[::-1]