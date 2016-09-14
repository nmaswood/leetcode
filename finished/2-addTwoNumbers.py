# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toNum(x):
            if x == []:
                return 0
            return int(''.join(x)[::-1])
            
        number1 = []
        while(l1):
            number1.append(str(l1.val))
            l1 = l1.next
        number2 = []
        while (l2):
            number2.append(str(l2.val))
            l2 = l2.next
        
        res = map(int, list(str(toNum(number1) + toNum(number2))))[::-1]
        
        head = ListNode(res[0])
        
        curr = head
        for num in res[1:]:
            
            curr.next = ListNode(num)
            curr= curr.next
        return head