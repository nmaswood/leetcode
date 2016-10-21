class Solution(object):
    def decodeString(self, s):

        def f(curr,acc,mul,temp_acc, looking_for_paren):

            if not curr:

                return acc

            first, rest = curr[0], curr[1:]

            if first.isdigit():

                return f(
                    rest,
                    acc, 
                    mul,
                    '', 

                    looking_for_paren)

            elif first == '[':

                return f(rest, acc, mul,temp_acc, True)

            elif first == ']':

                accPrime = mul * (temp_acc)

                return f(rest, accPrime, None, '', False)

            else:


                return f(rest, acc, mul, first + temp_acc, looking_for_paren)

        return f(s, '', None, '', False)


r = Solution()

r.decodeString('3[a]2[bc]')