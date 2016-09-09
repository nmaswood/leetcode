class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        foo = []
        while True:

            foo.append(str(self.val))
            the_next = self.next
            self.val = the_next
            if not the_next:
                break
            self.next = the_next.next

        return '\t'.join([x for x in foo if x is not None])


class Solution(object):

    def length(self,xs):
        if xs is None:
            return 0
        else:
            return 1 + self.length(xs.next)


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def sub(curr,index, n, head,prev):
            if index == n:

                next_n = curr.next if curr else None

                prev.next = next_n

                return head
            else:

                return sub(curr.next, index + 1, n, head, curr)
        if n == 0:
            return head.next
        elif head.next is None:
            return None
        else:
            return sub(head, 1, n, head, head)

a = ListNode(1)
b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)

a.next = b
#b.next = c
#c.next = d

r = Solution()
x = r.removeNthFromEnd(a,1)
print (x)
