# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseLinkedList(self, head,k, prev):

        i = 0

        while i < k:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
            i += 1

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        save = head
        i = 0
        prev = None
        while head:
            prev = head
            if i == m:
                self.reverseLinkedList(head, n - m,  prev)
                break
            head = head.next
            i += 1

