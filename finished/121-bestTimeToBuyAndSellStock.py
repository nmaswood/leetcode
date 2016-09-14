class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = len(prices)

        if l in [0,1]:
            return 0

        MAX = prices[1] - prices[0]

        prev_min = prices[0]

        for price in prices:

            diff = price - prev_min
            MAX = max(MAX, diff)
            prev_min = min(prev_min, price)

        return MAX
