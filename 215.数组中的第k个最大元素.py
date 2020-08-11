#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List
from heapq import heappop,heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heappush(heap,i)
            if len(heap)>k:
                heappop(heap)
        
        return heappop(heap)
# @lc code=end

