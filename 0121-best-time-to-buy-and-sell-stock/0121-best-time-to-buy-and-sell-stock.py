class Solution(object):
    
    def maxProfit(self,arr):
        maxPro = 0
        minPrice = float('inf')
        for i in range(len(arr)):
            minPrice = min(minPrice, arr[i])
            maxPro = max(maxPro, arr[i] - minPrice)
        return maxPro

