# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while(head and head.val == val):
            head = head.next
            
            
        saveHead = head
            
        while(head):
            
            nextHead = head.next
            if not nextHead:
                break
            
            nextHeadVal = nextHead.val
            if nextHeadVal == val:
                lookAhead = head.next
                while lookAhead and lookAhead.val == val:
                    lookAhead = lookAhead.next
                    
                head.next = lookAhead
            
            head = head.next
        return saveHead