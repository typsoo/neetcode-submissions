class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0

        suff = [0] * n
        suff[-1] = prices[-1]

        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], prices[i])

        res = 0

        mini = prices[0]
        for i in range(n-1):
            mini = min(mini, prices[i])
            res = max(res, suff[i+1] - mini)

        return res 