class Tree(object):

    def __init__(self, o, l,r):
        self.operator = o
        self.left = l
        self.right = r

class Solution(object):

    def init_strip(self,s):
        return  ''.join(s.split())

    def parse(self, s):

        first, rest = s[0], s[1:]

        if first in ["", None, []]:
            return 0

        elif first == "(":

            close_expression = 1
            expression = []

            for idx,letter in enumerate(rest):

                if letter == "(":
                    close_expression +=1
                elif letter == ")":
                    close_expression -=1
                else:
                    expression.append(letter)

                if close_expression == 0:
                    break

            expression_one = ''.join(expression)
            operator = rest[idx + 1]
            expression_two = self.parse(s[idx + 2:])

            return Tree(operator, expression_one, expression_two)

        else:
            print ('first', first)
            if len(rest) > 0:
                return Tree(rest[0], int(first), self.parse(rest[1:]))
            else:
                return Tree('+', 0, 0)

    def main(self, s):

        s_prime = self.init_strip(s)

        return self.parse(s_prime)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass


r = Solution()

x = r.main("1 + 1 - 1")


print (x.operator)
print (x.left)
right = x.right

print ("----")
print (right.operator)
print (right.left)
print (right.right)
