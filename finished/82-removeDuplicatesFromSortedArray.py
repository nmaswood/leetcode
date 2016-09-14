# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import Counter

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = set()
        values_order = []
        
        
        while(head):
            values_order.append(head.val)
            head = head.next
        
        counted = {k for (k,v) in Counter(values_order).items() if v != 1}
        
        fin_values = [x for x in values_order if x not in counted]
        

        if not fin_values:
            return
            
        head = ListNode(fin_values.pop(0))
        
        head_ref = head
        
        curr = head
        
        for val in fin_values:
            
            new_node = ListNode(val)
            
            curr.next = new_node
            
            curr = new_node
            
        return head
            
        
        
                
        