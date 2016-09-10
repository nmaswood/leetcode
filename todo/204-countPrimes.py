class Solution(object):
    def countPrimes(self, n):

        r = list(range(n))
        sieve = set()
        first = 2
        change = True
        save = 2

        while len(r) > 3 and change:

            r_prime = r[:save] + [x for x in r[save:] if x % first != 0]
            change = r_prime != r
            r = r_prime
            first += 1
            print (first)
            save += 1

        print (r)

r = Solution()
r.countPrimes(100)
