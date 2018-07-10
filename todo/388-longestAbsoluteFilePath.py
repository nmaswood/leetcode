from collections import deque
from pdb import set_trace

s = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"


class Tree():

    def __init__(self, val, children=None, is_root=False):
        if children is None:
            children = []

        self.val = val
        self.children = children
        self.is_root = is_root

    def __str__(self):
        acc = []
        stack = deque()
        stack.append((self, 0))
        depth = 0

        while stack:

            node, depth = stack.pop()
            acc.append('{}{}'.format('\t' * depth, node.val))

            for child in node.children:
                stack.append((child, depth + 1))

        return '\n'.join(acc)


    def __repr__(self):
        return str(self)


class Solution(object):

    def parse(self, input_str):
        tokens = input_str.split('\\n')
        root = Tree(None, None, True)
        head = root
        stack = deque()

        stack.append((head, 0))

        for token in tokens:
            token_depth = token.count('\\t') + 1
            token_stripped = token.lstrip('\\t')

            stack_head, stack_depth = stack[-1]

            set_trace()

            while stack_depth + 1 != token_depth:
                stack_head, stack_depth = stack.pop()

            new_node = Tree(token_stripped)
            stack_head.children.append(new_node)
            stack.append((new_node, stack_depth + 1))

        return root

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pass

sol = Solution()
