#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        print(nums)
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l = i+1
            h = len(nums)-1
            #output when ==0
            while(l<h):
                sum_= nums[i]+nums[l]+nums[h]
                if sum_ == 0:
                    result.append([nums[i],nums[l],nums[h]])
                    while(l<h and nums[l+1]==nums[l]):
                        l+=1
                    while(l<h and nums[h]==nums[h-1]):
                        h-=1
                    l+=1
                    h-=1
                elif sum_<0:
                    l+=1
                else:
                    h-=1
        print(type(result))
        return result

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = [0,0,0]
    print(s.threeSum(ary))

