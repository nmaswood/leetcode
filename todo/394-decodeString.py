class Solution(object):
    def decodeString(self, s):

        def f(curr,acc,mul, looking_for_paren):

            if not curr:
                return curr
            elif:
                first, rest = curr[0], curr[1:]

                if looking_for_paren and first == ']':
                    return (mul * acc) + f(rest, '', 1, False)
                elif first == '[':
                    return f(rest, '', mul, True)
                    return f(rest, acc + first, mul, True):
                elif first in [1,2,3,4,5,6,7,8,9]:
                    return f(rest, acc, mul + first, looking_for_paren)
                else:
                    return f(rest, acc + first, mul, False)
