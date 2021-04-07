# dp bottom-up
# F(amount) = F(amount - coin) + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        dp += [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
