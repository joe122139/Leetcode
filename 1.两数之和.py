#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dct:
                return (dict[target])
        
# @lc code=end

