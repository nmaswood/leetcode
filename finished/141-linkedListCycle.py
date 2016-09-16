# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False


        slowRunner = head
        fastRunner = head.next

        while slowRunner and fastRunner:

            if slowRunner.val == fastRunner.val:
                return True

            slowRunner = slowRunner.next
            fastRunner = fastRunner.next
            if not fastRunner:
                return False
            else:
                fastRunner = fastRunner.next

        return False







