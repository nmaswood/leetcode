from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = list()
        chars = ["(", "{", "["]
        other_half = [")", "}", "]"]
        the_dict = dict(zip(chars,other_half))


        for char in s:

            if char in chars:
                stack.append(char)
            elif char in other_half:

                popped_off = stack.pop()

                if the_dict[popped_off] == popped_off:
                    return False

        if len(stack):
            return False

        return True
