class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.children = []

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.val)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

class Solution(object):

    def createList(self, strs):

        max_len = len(max(strs, key = len))

        d = {i:set() for i in range(max_len + 1)}

        for word in strs:

            for index,letter in enumerate(word):

                d[index].add(letter)

            d[index + 1].add('')

        return [d[i] for i in range(max_len)]

    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str]
        :rtype: st
        """
        d = self.createList(strs)

        def f(curr, letters):

            if not letters:
                return curr
            else:
                first, rest = letters[0], letters[1:]
                if len(first) == 1:
                    curr.val += first.pop()
                    return f(curr, rest)
                else:
                    acc = []
                    for val in first:
                        if val == '':
                            acc.append(ListNode(''))
                        else:
                            acc.append(f(ListNode(val), rest))
                    curr.children = acc
                    return curr

        HEAD = ListNode('START')
        first_init, rest_init = d[0], d[1:]

        HEAD.children = [f(ListNode(x),rest_init) for x in first_init]
        vals = [x.val for x in HEAD.children]

        print (HEAD)

        return max (vals, key = len)


r = Solution()
res = r.longestCommonPrefix(['aaab', 'aaa', 'aaac', 'aa', 'aab', 'a', 'bb','b'])
print (res)

