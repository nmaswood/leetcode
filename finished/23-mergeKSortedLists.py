import heapq as h

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        for LinkedList in lists:
            while(LinkedList):
                h.heappush(heap, LinkedList.val)
                LinkedList = LinkedList.next

        res = []
        while (heap):
            res.append(h.heappop(heap))
        return res
