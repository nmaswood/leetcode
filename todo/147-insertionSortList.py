# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def insertionSortList(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """

        def sub(head, curr,prev,prev_val):

            if curr is None:
                return head

            current_val = curr.val

            if prev:
                if prev_val <= current_val:
                    return sub(head, curr.next, curr, current_val)
                else:
                    save_next = curr.next
                    curr.next = prev
                    prev = curr

                    return sub(head, save_next, curr, current_val)







