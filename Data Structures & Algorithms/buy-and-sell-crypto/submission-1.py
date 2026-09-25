class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)



        mini = prices[0]
        res = 0
        for i in range(n):
            mini = min(mini, prices[i])
            res = max(res, prices[i] - mini)

        return res 