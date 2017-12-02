from pdb import set_trace
from collections import deque

class TreeNode(object):

    def __str__(self):
        str_builder = []
        q = deque()


        if not self:
            return 'EMPTY'

        q.append([0, self])
        sb = {}
        max_level = 0

        while q:
            level, node = q.popleft()
            max_level = max(max_level, level)

            if level not in sb:
                sb[level] = []

            sb[level].append(str(node.val))

            if node.left:
                q.append([level + 1, node.left])
            if node.right:
                q.append([level + 1, node.right])

        sb_prime = []
        for i in range(max_level + 1):
            sb_prime.append('\t' * max(int(int(max_level + 1 / 2) - i), 0))
            sb_prime.append('  '.join(sb[i]))
            sb_prime.append('\n')
        s = ''.join(sb_prime)
        print(s)
        return s


    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    @staticmethod
    def sum_value(node1, node2):
        value = 0
        value += node1.val if node1 else 0
        value += node2.val if node2 else 0
        return value

    @staticmethod
    def left_or_none(node):
        if node:
            return node.left
        return None

    @staticmethod
    def right_or_none(node):
        if node:
            return node.right
        return None

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        q = deque()
        q.append(['left', t1,t2])
        new = True
        prev = TreeNode(0)
        head = prev

        while q:
            direction, node1, node2 = q.popleft()
            if not node1 and not node2:
                break
            value = Solution.sum_value(node1, node2)
            new_node = TreeNode(value)

            if direction == 'left':
                prev.left = new_node
            else:
               prev.right = new_node

            q.append(['left', Solution.left_or_none(node1), Solution.left_or_none(node2)])
            q.append(['right', Solution.right_or_none(node1), Solution.right_or_none(node2)])

            prev = new_node
        set_trace()


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
c.left = d

s = Solution()
