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

    def isPalindrome(self, head):
        acc = []

        while (head):
            acc.append(head.val)
            head = head.next

        rev = acc[::-1]

        for forward, backward in zip(acc,rev):
            if forward != backward:
                return False
        return True


"""
r = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(1)

a.next = b
b.next = c

res = r.isPalindrome(a)
print (res)
"""
