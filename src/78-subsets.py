from itertools import combinations

class Solution0():

    """
    O(exp) Time O(exp) Space

    Explanation:
    Let Python do the work for you, there is a method called combinations
    in itertools that generates all subsets of length k for a list n.

    Simply call this method from i = [0...len(n)) and store all the results
    combinations returns to you in a set.

    """

    def subsets(self, nums):

        acc = set()

        for i in range(len(nums) + 1):

            acc |= set(combinations(nums, i))

        return acc

class Solution(object):
    """

    Explanation: Build a tree and collect every node

                [1,2,3]
            /      |     \

        [1,2]    [1,3]  [2,3]

     /  |        /  |      |  \
    [1] [2]    [1] [3]    [2] [3]

   For a List L remove the item at each index i
   and recurse on new list, the list without item i.
   For every function call add the current node into the set.

   Because you are adding to a set() there will be no duplicates

    """

    def pluck(self, l, delete):

        """
        O(n) Time O(n) space

        This returns the a new list l prime without the item
        at the index delete

        """

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

        return list(seen)


r = Solution()

a = [1,2,3]
print (r.subsets(a))
