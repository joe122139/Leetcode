#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
import heapq 
from heapq import heappop
from heapq import heappush

class Point(object):
    def __init__(self,x,y,dis):
        self.x = x
        self.y = y
        self.dis = dis
    
    def __lt__(self,other):
        return self.dis > other.dis
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        result=[]
        for x,y in points:
            dis = x*x + y *y
            heappush(h,Point(x,y,dis))
            if len(h)>K: heappop(h)
        

        for i in range(K):
            p = heappop(h)
            result.append([p.x,p.y])
        return result


        
# @lc code=end

