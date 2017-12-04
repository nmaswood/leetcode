from pdb import set_trace
from collections import deque

# class TreeNode(object):

    # def __repr__(self):
        # return str(self)

    # def __str__(self):
        # str_builder = []
        # q = deque()


        # if not self:
            # return 'EMPTY'

        # q.append([0, self])
        # sb = {}
        # max_level = 0

        # while q:
            # level, node = q.popleft()
            # max_level = max(max_level, level)

            # if level not in sb:
                # sb[level] = []

            # sb[level].append(str(node.val))

            # if node.left:
                # q.append([level + 1, node.left])
            # if node.right:
                # q.append([level + 1, node.right])

        # sb_prime = []
        # for i in range(max_level + 1):
            # sb_prime.append('\t' * max(int(int(max_level + 1 / 2) - i), 0))
            # sb_prime.append('  '.join(sb[i]))
            # sb_prime.append('\n')
        # s = ''.join(sb_prime)
        # return s


    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

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

    @staticmethod
    def deepcopy(tree):
        head = TreeNode("ROOT")
        q = deque()

        q.append(['left', tree, head])

        while q:
            direction, node, parent = q.popleft()
            new_node = TreeNode(node.val)

            if node.left:
                q.append(['left', node.left, new_node])

            if node.right:
                q.append(['right', node.right, new_node])

            if direction == 'left':
                parent.left = new_node
            else:
                parent.right = new_node

        return head.left

    def mergeTrees(self, t1, t2):

        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        head = TreeNode("ROOT")
        q = deque()

        q.append(['left', t1,t2, head])

        while q:
            direction, node1, node2, parent = q.popleft()
            if not node1 and not node2:
                break

            new_value = Solution.sum_value(node1, node2)
            new_node = TreeNode(new_value)

            if (node1 and node1.left) or (node2 and node2.left):
                q.append(['left', Solution.left_or_none(node1), Solution.left_or_none(node2), new_node])

            if (node1 and node1.right) or (node2 and node2.right):
                q.append(['right', Solution.right_or_none(node1),Solution.right_or_none(node2), new_node])

            if direction == 'left':
                parent.left = new_node
            else:
                parent.right = new_node

        return head.left

def createTree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    c.left = d
    return a

t1 = createTree()
t2 = createTree()

s = Solution()
x = s.mergeTrees(t1,t2)
print (t1)
print (x)

