class Solution:
    # TC : O(n)
    # SC : O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices)==0:
            return 0
        i = 1
        resprofit = 0
        n = len(prices)
        while i < n:
            val = prices[i]-prices[i-1]
            if resprofit + val > resprofit:
                # print(prices[i],prices[i-1],i)
                resprofit += val
                i += 1
            else:
                i += 1
        return resprofit
        