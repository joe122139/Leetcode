#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        size=len(nums)
        if size==0:
            return 0
        sum=nums[0]
        max_val=sum
        for i in range(1,size):
            sum = max(sum+nums[i],nums[i])
            if(sum>max_val):
                max_val= sum
        
        return max_val
            
        
# @lc code=end

