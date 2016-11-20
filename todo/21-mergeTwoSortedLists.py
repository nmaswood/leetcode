class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def sub(head, current, l1_rest, l2_rest):


            if l1_rest is None:
                current.next = l2_rest
                return head

            elif l2_rest is None:

                current.next = l1_rest
                return head

            l1_val, l2_val = l1_rest.val, l2_rest.val

            if l1_val >= l2_val:
                current.next = ListNode(l2_val)
                return sub(head, current.next, l1_rest, l2_rest.next)
            else:
                current.next = ListNode(l1_val)
                return sub(head, current.next, l1_rest.next, l2_rest)

        if l1 is None and l2 is None:
            return None
        dummy = ListNode(1234)

        return sub(dummy,dummy, l1,l2).next


a = ListNode(10)
b = ListNode(20)
c = ListNode(30)

d = ListNode(5)
e = ListNode(15)
f = ListNode(20)

