#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from heapq import heappop,heappush
from collections import Counter
from typing import List
class FreqNum(object):
    def __init__(self,freq,num):
        self.num = num
        self.freq = freq
    
    def __lt__(self,other):
        if self.freq != other.freq:
            return self.freq < other.freq  # self.freq<other.freq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h =[]
        for key,cnt in counter.items():
            heappush(h,FreqNum(cnt,key))
            if(len(h)>k):
                heappop(h)
        
        return [heappop(h).num for _ in range(k)][::-1]

# @lc code=end

