LITERAL = 0, EXPRESSION = 1

class Literal(object):

    def __init__(self, value):

        self.value = value

class Expression(object):

    def __init__(self, operand, left, right):

        self.operand = operand
        self.left = left
        self.right = right

class Tree(object):

    def __init__(self, enum,value ):
        self.ENUM = enum
        self.value = value

class Solution(object):

    def parse(self, s, acc, prev):

        if not s:
            return

        first, rest = s[0], s[1:]

        if first == '+':

            expression = Expression(first, prev, parse(rest))

            return Tree(EXPRESSION, expression)

        if first == '(':

            return Tree(EXPRESSION, parse(rest, acc,





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
