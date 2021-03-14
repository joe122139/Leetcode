# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]        
        n = len(nums)
        def dfs(S,nums):
            if not nums:
                result.append(S)
            for i in range(len(nums)):
                pre = nums[:i]
                post = nums[i+1:]
                print('pre:',pre,'post:',post,'S:',S)
                dfs(S+[nums[i]],pre+post)
                

        dfs([],nums)
        return result
# @lc code=end

