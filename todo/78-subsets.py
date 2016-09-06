class Solution(object):
    def partition(self, l,i):

        return l[:i] + l[i+1:]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        acc = [[]]

        def sub(input_list):

            if input_list == []:
                return

            acc.append(input_list)

            for i in range(0, len(input_list)):

                new_list = self.partition(input_list,i)
                print (new_list)
                sub(new_list)

        sub(nums)
        return acc

r = Solution()

a = [1,2,3]

print (r.subsets(a))
