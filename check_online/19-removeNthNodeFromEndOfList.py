class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):

        temp = self
        foo = []
        while temp:
            foo.append(str(temp.val))
            temp = temp.next

        return '\t'.join([x for x in foo if x ])


class Solution(object):

    @staticmethod
    def length(the_list):
        index  = 0
        head = the_list
        while head:
            index += 1
            head = head.next
        return index

    def removeNthFromEnd(self, head, n):

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = Solution.length(head)
        exclude = length - n
        index = 0

        temp = head

        while temp:
            index += 1
            if index == exclude:
                temp.next = temp.next.next
            temp = temp.next

        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

r = Solution()
x = r.removeNthFromEnd(a, 3)
print (x)
