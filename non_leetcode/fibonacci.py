class Solution():

    def recursive(self, n):

        def f(x):
            if x in [0,1]:
                return x
            return f(x-1) + f(x-2)

        return f(n)

    def iterative(self, n):

        array = [0 for _ in range(n+1)]
        array[1] = 1

        for i in range(2, n + 1):

            array[i] = array[i-1] + array[i-2]

        return array[n]

    def iterative_2(self, n):
        a = 0
        b = 1
        for _ in range(1, n + 1):
            tmp = b
            b += a
            a = tmp
        return a

r = Solution()
res1 = r.recursive(5)
res2 = r.iterative(5)
res3 = r.iterative_2(5)

print (res1, res2,res3)
