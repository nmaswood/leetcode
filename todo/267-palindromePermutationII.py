from collections import Counter

class Solution(object):
    def ins_into(self, l,index,item):

        return l[index:] + [item] + l[:index]

    def item_and_list(self,l, index):

        return l.pop(index), l

    def permute(self, nums):

        l = len(nums)
        if l in [0,1]:
            return [nums]

        acc = [
            [nums[0]],
        ]

        def f(curr, acc, vals):

            if not curr:
                return acc

            first, rest = curr[0], curr[1:]

            accPrime = []
            if acc == []:
                return f(rest, [first])

            for thing in acc:
                l = len(thing)
                for index in range(l + 1):
                    res = self.ins_into(thing, index, first)
                    asTuple = tuple(res)
                    if asTuple in vals:
                        pass
                    else:
                        accPrime.append(res)

                    vals.add(asTuple)

            return f(rest, accPrime,vals)

        return f(nums[1:], acc, set(tuple([nums[0]])))

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        x = Counter(s)
        if not sum(v % 2 for v in x.values()) < 2:
            return []
        acc = []
        odd = ''
        for k,v in x.items():

            if v % 2 == 0:

                acc.append((k) * int(v / 2))
            else:
                odd = k * v

        big_string = ''.join(acc)


        permutations = self.permute(big_string)
        as_strs = [''.join(x) for x in permutations]


        res = [x + x[::-1] for x in as_strs]
        return res


r = Solution()
res = r.generatePalindromes('aabbccc')
print (res)

