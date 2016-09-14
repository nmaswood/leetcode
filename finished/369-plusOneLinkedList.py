# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        acc = []
        save = head
        
        while(save):
            acc.append(save.val)
            save = save.next
            
        acc = map(int,list(str(int(''.join(map(str,acc))) + 1)))
            
        head = ListNode(acc.pop(0))
        
        save_head = head
        
        while acc:
            save_head.next = ListNode(acc.pop(0))
            save_head = save_head.next
        
        return head