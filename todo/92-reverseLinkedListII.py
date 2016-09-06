class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        a = []
        while self:
            a.append(str(self.val))
            self = self.next

        return '\t'.join(a)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        index = 0
        curr = head

        prev = None

        while curr:

            if index > m and index  < n:
                save_next = curr.next
                curr.next = prev
                prev = curr
                curr = save_next
            index += 1

        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

r = Solution()
r.reverseBetween(a,2,4)
print(a)

