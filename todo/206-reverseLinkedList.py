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
    def reverseList(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            save_next = head.next
            head.next = prev
            prev = head
            head = save_next
        return prev

"""
u = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

a.next = b
b.next = c


print (a)

r.reverseList(a)

print(c)
"""
