#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# @lc code=start
from typing import List 
import numpy as np
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        revert = 0
        size = len(nums)
        t = 0
        i = size-2
        j=0
        # from LSB to MSB
        while(i>=0):
            if(revert==1):
                break
            j = size-1
            while(j>i):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    revert =1
                    t=i
                    break
                j-=1
            i-=1
        #ascend sort the rest
        for i in range(t+1,size-1):
            for j in range(i+1,size):
                if(nums[i]>nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]

        #if not swap has occurred
        if(revert==0):  
            nums.sort()

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = [1,2]
    s.nextPermutation(ary)
    print(ary)

