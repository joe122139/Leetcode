#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        f = np.zeros(size)
        f[0] = 0
        min_ = prices[0]
        for i in range(1,size):
            f[i] = max(f[i-1],prices[i]-min_)
            if (prices[i]<min_):
                min_ = prices[i]
        
        return int(f[size-1])
        
# @lc code=end

