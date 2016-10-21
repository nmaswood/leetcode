class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        saveHead = head


        swap = True



        while curr.next:

            if swap:

                saveCurr =  curr.val
                saveNext =  curr.next.val

                curr.val = saveNext
                curr.next.val = saveCurr

            swap =  not swap
            curr.next = nextNext

        return head
