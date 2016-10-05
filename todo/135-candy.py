class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        acc = [0 for _ in range(len(ratings))]

        acc[0] = 1

        for index, current_rating in enumerate(ratings[1:]):

            index = index + 1

            prev = ratings[index - 1]

            if prev == current_rating:
                print ('HERE')
                acc[index] = acc[index - 1]
            elif prev > current_rating:
                print ('THERE')
                acc[index] = 1
                acc[index - 1] += 1
            else:
                print ('THIS')
                acc[index] = acc[index - 1] + 1

        return sum(acc)


r = Solution()

res = r.candy([2,1])
print (res)
