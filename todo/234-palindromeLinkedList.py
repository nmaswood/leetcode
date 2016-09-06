from collections import Deque
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):

        """
        :type head: ListNode
        :rtype: bool
        """
        def traverse(head, stack):
            if head is None:
                return stack
            else:
                stack.append(head.val)
                return traverse(head.next, stack)

        def sub(head, stack,index, halfway, odd):

            if head is None:
                return True

            if index >=
