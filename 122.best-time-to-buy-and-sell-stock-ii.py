#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        size = len(prices)
        f = np.zeros([size,2])
        ## asset obtain on ith's day when having nostock
        # f[i][0]

        ## asset obtain on ith's day when having stock
        # f[i][1]

        ## on the day 0, has no stock, so asset is 0
        f[0][0] = 0
        ## on the day 0, has stock, so asset is 0 - prices[0]
        f[0][1] = 0-prices[0]
        for i in range(1,size):
            f[i][0] = max(f[i-1][0], f[i-1][1]+prices[i])
            f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i])

        return int(f[size-1][0])

        #ith's day has stock
        
# @lc code=end

