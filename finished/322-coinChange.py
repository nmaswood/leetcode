class Solution(object):
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0

        num_coins = len(coins)
        if num_coins == 1:
            x = amount % coins[0] == 0
            if x:
                return int(amount / coins[0])
            else:
                return -1

        memo = [float('inf')] * amount

        for coin in coins:
            if coin <= amount:
                memo[coin - 1] = 1

        for memo_index in range(amount):
            for coin_index in range(num_coins):

                modify_index = memo_index - coins[coin_index]

                if modify_index >= 0:
                   memo[memo_index] = min(
                        memo[memo_index],1 + memo[modify_index]
                    )

        if memo == []:
            return -1

        last = memo[-1]

        if last == float('inf'):
            return -1
        else:
            return last


r = Solution()

x = r.coinChange([1], 1)

