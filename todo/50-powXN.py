class Solution(object):
    def myPow(self, x, n):


        def recurse(x_prime,n_prime):


            if n_prime == 0:
                return 1
            if n_prime == 1:
                return x_prime
            if n_prime == 2:

                return x_prime * x_prime


            even = n_prime % 2 == 0

            half = int(n_prime / 2)


            if even:

                return recurse(x_prime, half)  * recurse(x_prime, half)
            else:

                return recurse(x_prime, half) * recurse(x_prime, half) * x_prime

        return recurse(x,n)


r = Solution()

res = r.myPow(11,12)

print (res)