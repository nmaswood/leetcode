class Solution(object):
    def pluck(self, l, delete):

        return tuple(x for i,x in enumerate(l) if i != delete)


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        seen = set()
        seen.add(())

        def sub(input_list):

            if not input_list:
                return

            seen.add(input_list)

            for i in range(len(input_list)):

                plucked = self.pluck(input_list, i)

                if plucked not in seen:

                    sub(plucked)
        sub(tuple(nums))
        print(seen)
        return list(seen)





r = Solution()

a = [1,2,3]
print (r.subsets(a))
