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

        def f(curr, acc):

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
                    accPrime.append(res)

            return f(rest, accPrime)

        return f(nums[1:], acc)


r = Solution()
res = r.permute([1,2,3,4])
print (res)


