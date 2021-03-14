#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 0: have stocks, sold 0 time.
        # 1: no stocks, sold 1 time.
        # 2: have stocks, sold 1 time.
        # 3: no stocks, sold 2 times.

        size = len(prices)
        buy2 = buy1 = -prices[0]
        sell1, sell2 = 0,0

        for i in range(1,size):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2+ prices[i])
        
        return sell2
        
# @lc code=end

