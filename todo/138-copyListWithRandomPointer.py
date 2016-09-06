class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):


    def listStoreFromNode(self, node):

        random_node = self.random

        if random_node is None:
            return 'Empty', 'Empty'

        random_label = random_node.label
        next_from_random = random_node.next

        if next_from_random is None:
            return 'None', random_label

        return next_from_random.label, random_label


    def copyRandomList(self, head):

        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def create_dict():

            curr = head

            d  = {}

            while curr:
                key, value = self.listStoreFromNode(curr)
                d[key] = value
                curr = curr.next
            return d

        populated = create_dict()

        def create_list():

            first_node = Listd['None']




