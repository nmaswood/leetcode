"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution(object):

    def listToNumber(self, l):

        def listToNumberSub(l, acc):

            if l is None:

                if acc == []:
                    return 0
                else:
                    return int(''.join(acc)[::-1])
            else:
                acc.append(str(l.val))
                return listToNumberSub(l.next, acc)

        return listToNumberSub(l, [])

    def numToStrList(self, num):
        return list(str(num))

    def numberToList(self, numAsList):

        def numberToListSub(numAsList, head, acc):

            if numAsList == []:
                return head.next
            else:
                first = int(numAsList[0])
                rest = numAsList[1:]

                newNode = ListNode(first)
                acc.next = newNode

                return numberToListSub(rest, head, acc.next)

        dummy = ListNode('')

        return numberToListSub(numAsList, dummy, dummy)

    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        the_sum = self.listToNumber(l1) + self.listToNumber(l2)

        as_str_list = self.numToStrList(the_sum)[::-1]
        print (as_str_list)

        return self.numberToList(as_str_list)
"""
r = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

x = r.listToNumber(a)
y = r.addTwoNumbers(a,a)
print (r.listToNumber(y))
print(x)




"""
