# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def sub(head, current, prev, seen):

            if current is None:
                return head

            node_val = current.val

            if node_val in seen:

                prev.next = current.next
                return sub(head, current.next, prev, seen)
            else:
                seen.add(node_val)
                return sub(head, current.next, current, seen)

        return sub(head, head, None, set())
