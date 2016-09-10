class Solution(object):

    def __init__(self):

        self.vals = set()
        self.vals.add(())

    def pluck(self, x, i):

        return x[:i] + x[i+1:]

    def pluck_all(self,x):

        l = len(x)
        return [self.pluck(x,i) for i in range(l)]

    def subsetsWithDup(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def process(sub_nums):

            if sub_nums == []:
                return
            else:
                hashable_big = tuple(sub_nums)
                if hashable_big not in self.vals:
                    self.vals.add(hashable_big)

                for sub_list in self.pluck_all(sub_nums):

                    hashable = tuple(sub_list)

                    if hashable not in self.vals:

                        self.vals.add(hashable)
                        process(hashable)
        process(nums)

        print (set([set(x) for x in self.vals]))
r = Solution()
r.subsetsWithDup([1,2,2])
