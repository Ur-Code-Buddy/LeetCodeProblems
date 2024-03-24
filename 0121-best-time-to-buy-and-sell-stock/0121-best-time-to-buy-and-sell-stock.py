class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxP = 0
        length = len(prices)
        
        while r < length:
            if prices[l] < prices[r]:
                if prices[r] - prices[l] > maxP:
                    maxP = prices[r] - prices[l]
                #maxP = max(maxP, prices[r] - prices[l])
            else: l = r
                
            r += 1
            
        return maxP
                
        
        
        