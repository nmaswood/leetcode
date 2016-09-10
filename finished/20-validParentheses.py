from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2:
            return False


        s = s.strip()
        stack = list()
        chars = ["(", "{", "["]
        other_half = [")", "}", "]"]
        the_dict = dict(zip(chars,other_half))


        for char in s:

            if char in chars:
                stack.append(char)
            elif char in other_half:
                if len(stack) == 0:
                    return False
                popped_off = stack.pop()
                expecting = the_dict[popped_off]

                if expecting != char:
                    return False

        if len(stack):
            return False

        return True

# r = Solution()
# print (r.isValid("([)]"))
