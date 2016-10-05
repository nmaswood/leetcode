class Solution(object):

    def perfectSquaresLessThanK(self, k):

        assert k > 0
        acc = []

        val = 1
        idx = 1

        while val <= k:

            acc.append(val)
            idx += 1
            val = (idx * idx)

        return acc

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        perfectSquares = self.perfectSquaresLessThanK(n)

        DP = [float('inf') for _ in range(n + 1)]

        for square in perfectSquares:
            DP[square - 1] = 1

        print (DP)


        for number in range(n+ 1):
            for square_index, square in enumerate(perfectSquares):


                memo_index = number - square
                other = DP[number - square]

                print ("number", number)
                print ('curr', DP[number])
                print ('memo_index', memo_index)
                print ('square', square)
                print ('other', other)
                print (DP)
                print ("----\n")

                DP[number] = min(DP[number], 1 + other)

        print (DP)
        return DP[-1]


r = Solution()
res = r.numSquares(4)
print (res)






