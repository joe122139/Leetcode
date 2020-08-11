#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List


#implementation of the monotonicQueue from a min heap
class MonotonicQueue(object):
    def __init__(self):
        self.__data =[]

    def push(self,e,nums):
        size = len(self.__data)
        while size > 0 and nums[e] >= nums[self.__data[size-1]]:
            self.__data.pop(size-1)
            size-=1
        self.__data.append(e)

    def pop(self):
        popped = self.__data.pop(0)
        return popped
    
    def max(self):
        return self.__data[0]
    
    def print(self,nums):
        for i in self.__data:
            print(nums[i], end=' ') 
        print()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = MonotonicQueue()
        result=[]
        size = len(nums)
        for i,it in enumerate(nums):
            if(i>=k and i-k>=h.max()):
                h.pop()
            h.push(i,nums)
            if(i-k+1 >= 0):
                result.append(nums[h.max()])
        
        return result

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    #ary = [[1,4,5],[1,3,4],[2,6]]
    #ary = ["i", "love", "leetcode", "i", "love", "coding","love","love","luca","wang"]
    #ary = [1,3,-1,-3,5,3,6,7]
    #ary = [1,3,-1,-3,5,3,6,7]
    #ary = [1,-9,8,-6,6,4,0,5]
    ary = [8,-6,6,4,0,5]
    print(s.maxSlidingWindow(ary,4))


