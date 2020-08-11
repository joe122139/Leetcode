#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pt_a =0
        pt_b =1
        while(pt_b<len(nums)):
            if(nums[pt_a]!=nums[pt_b]):
                pt_a+=1
                nums[pt_a]=nums[pt_b]
            pt_b+=1
        return pt_a+1

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    ary = [1,1,2]
    print(s.removeDuplicates(ary))
