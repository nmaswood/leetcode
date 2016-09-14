class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        init = {i:0 for i in range(length)}

        for sub_list in updates:

            left, right, update = sub_list
            for i in range(left,right + 1):
                init[i] = init.get(i,0) + update

        return [init[i] for i in range(length)]


r = Solution()
res = r.getModifiedArray(5, [[1,3,2], [2,4,3],[0,2,-2]])
print (res)
