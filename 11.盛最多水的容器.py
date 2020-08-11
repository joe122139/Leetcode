#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxVol = 0;
        j = length-1
        i = 0
        while(i<j):
            min_ = min(height[i],height[j])
            temp = min_*(j-i)
            if(maxVol<temp):
                maxVol = temp
            if(height[i]>height[j]):
                j-=1
            else:
                i+=1

        return maxVol


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    ary = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(ary))

